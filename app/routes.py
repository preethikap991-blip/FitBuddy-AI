from pathlib import Path
from fastapi import APIRouter, Depends, Form, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import select
from sqlalchemy.orm import Session

from .database import get_db
from .gemini_flash_generator import generate_nutrition_tip_with_flash
from .gemini_generator import generate_workout_gemini
from .models import Plan, User
from .schemas import FeedbackRequest, UserInput
from .updated_plan import update_workout_plan

BASE_DIR = Path(__file__).resolve().parent.parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))
router = APIRouter()


def _get_user(db: Session, user_id: str) -> User | None:
    return db.scalar(select(User).where(User.user_id == user_id))


def _result_context(user: User, plan: Plan, message: str | None = None) -> dict:
    return {
        "username": user.username,
        "user_id": user.user_id,
        "age": user.age,
        "weight": user.weight,
        "goal": user.goal,
        "intensity": user.intensity,
        "workout_plan": plan.updated_plan or plan.original_plan,
        "original_plan": plan.original_plan,
        "nutrition_tip": plan.nutrition_tip,
        "message": message,
    }


@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"title": "FitBuddy"},
    )


@router.post("/generate-workout", response_class=HTMLResponse)
def generate_workout(
    request: Request,
    username: str = Form(...),
    user_id: str = Form(...),
    age: int = Form(...),
    weight: float = Form(...),
    goal: str = Form(...),
    intensity: str = Form(...),
    db: Session = Depends(get_db),
):
    data = UserInput(
        username=username,
        user_id=user_id,
        age=age,
        weight=weight,
        goal=goal,
        intensity=intensity,
    )

    user = _get_user(db, data.user_id)
    if user is None:
        user = User(
            user_id=data.user_id,
            username=data.username,
            age=data.age,
            weight=data.weight,
            goal=data.goal,
            intensity=data.intensity,
        )
        db.add(user)
        db.flush()
    else:
        user.username = data.username
        user.age = data.age
        user.weight = data.weight
        user.goal = data.goal
        user.intensity = data.intensity

    workout_plan = generate_workout_gemini(
        data.username, data.age, data.weight, data.goal, data.intensity
    )
    nutrition_tip = generate_nutrition_tip_with_flash(data.goal)

    plan = db.scalar(select(Plan).where(Plan.user_id == data.user_id))
    if plan is None:
        plan = Plan(
            user_id=data.user_id,
            original_plan=workout_plan,
            nutrition_tip=nutrition_tip,
        )
        db.add(plan)
    else:
        plan.original_plan = workout_plan
        plan.updated_plan = None
        plan.feedback = None
        plan.nutrition_tip = nutrition_tip

    db.commit()
    db.refresh(user)
    db.refresh(plan)

    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context=_result_context(user, plan),
    )


@router.post("/submit-feedback", response_class=HTMLResponse)
def submit_feedback(
    request: Request,
    user_id: str = Form(...),
    feedback: str = Form(...),
    db: Session = Depends(get_db),
):
    user = _get_user(db, user_id)
    plan = db.scalar(select(Plan).where(Plan.user_id == user_id))

    if user is None or plan is None:
        raise HTTPException(status_code=404, detail="User or workout plan not found.")

    payload = FeedbackRequest(user_id=user_id, feedback=feedback)
    revised = update_workout_plan(
        plan.original_plan,
        payload.feedback,
        user.username,
        user.goal,
        user.intensity,
    )

    plan.updated_plan = revised
    plan.feedback = payload.feedback
    db.commit()
    db.refresh(plan)

    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context=_result_context(
            user,
            plan,
            message="Your workout plan has been updated using your feedback.",
        ),
    )


@router.get("/view-all-users", response_class=HTMLResponse)
def view_all_users(request: Request, db: Session = Depends(get_db)):
    users = db.scalars(select(User).order_by(User.created_at.desc())).all()
    return templates.TemplateResponse(
        request=request,
        name="all_users.html",
        context={"title": "All Users", "users": users},
    )


@router.get("/health")
def health():
    return {"status": "ok", "service": "FitBuddy"}


@router.post("/api/generate-workout")
def api_generate_workout(data: UserInput, db: Session = Depends(get_db)):
    user = _get_user(db, data.user_id)
    if user is None:
        user = User(
            user_id=data.user_id,
            username=data.username,
            age=data.age,
            weight=data.weight,
            goal=data.goal,
            intensity=data.intensity,
        )
        db.add(user)
        db.flush()
    else:
        user.username = data.username
        user.age = data.age
        user.weight = data.weight
        user.goal = data.goal
        user.intensity = data.intensity

    workout = generate_workout_gemini(
        data.username, data.age, data.weight, data.goal, data.intensity
    )
    tip = generate_nutrition_tip_with_flash(data.goal)

    plan = db.scalar(select(Plan).where(Plan.user_id == data.user_id))
    if plan is None:
        plan = Plan(user_id=data.user_id, original_plan=workout, nutrition_tip=tip)
        db.add(plan)
    else:
        plan.original_plan = workout
        plan.updated_plan = None
        plan.feedback = None
        plan.nutrition_tip = tip

    db.commit()

    return {
        "user_id": data.user_id,
        "username": data.username,
        "goal": data.goal,
        "intensity": data.intensity,
        "workout_plan": workout,
        "nutrition_tip": tip,
    }


@router.post("/api/submit-feedback/{user_id}")
def api_submit_feedback(
    user_id: str,
    payload: FeedbackRequest,
    db: Session = Depends(get_db),
):
    if payload.user_id != user_id:
        raise HTTPException(status_code=400, detail="User ID mismatch.")

    user = _get_user(db, user_id)
    plan = db.scalar(select(Plan).where(Plan.user_id == user_id))
    if user is None or plan is None:
        raise HTTPException(status_code=404, detail="User or workout plan not found.")

    revised = update_workout_plan(
        plan.original_plan, payload.feedback, user.username, user.goal, user.intensity
    )
    plan.updated_plan = revised
    plan.feedback = payload.feedback
    db.commit()

    return {"user_id": user_id, "updated_plan": revised}


@router.get("/api/users")
def api_users(db: Session = Depends(get_db)):
    users = db.scalars(select(User).order_by(User.created_at.desc())).all()
    return [
        {
            "user_id": user.user_id,
            "username": user.username,
            "age": user.age,
            "weight": user.weight,
            "goal": user.goal,
            "intensity": user.intensity,
        }
        for user in users
    ]


@router.get("/api/users/{user_id}")
def api_user(user_id: str, db: Session = Depends(get_db)):
    user = _get_user(db, user_id)
    plan = db.scalar(select(Plan).where(Plan.user_id == user_id))
    if user is None or plan is None:
        raise HTTPException(status_code=404, detail="User not found.")

    return {
        "user": {
            "user_id": user.user_id,
            "username": user.username,
            "age": user.age,
            "weight": user.weight,
            "goal": user.goal,
            "intensity": user.intensity,
        },
        "plan": {
            "original_plan": plan.original_plan,
            "updated_plan": plan.updated_plan,
            "feedback": plan.feedback,
            "nutrition_tip": plan.nutrition_tip,
        },
    }
