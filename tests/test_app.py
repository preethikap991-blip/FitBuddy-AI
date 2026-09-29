import os

os.environ["DEMO_MODE"] = "true"
os.environ["DATABASE_URL"] = "sqlite:///./test_fitbuddy.db"

from fastapi.testclient import TestClient
from app.main import app

# Using TestClient as a context manager runs FastAPI's lifespan, which creates
# the SQLite tables before requests are made.
with TestClient(app) as client:

    def test_health():
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "ok"


    def test_home_page():
        response = client.get("/")
        assert response.status_code == 200
        assert "FitBuddy" in response.text


    def test_generate_workout_page():
        response = client.post(
            "/generate-workout",
            data={
                "username": "Test User",
                "user_id": "TEST001",
                "age": "20",
                "weight": "60",
                "goal": "general wellness",
                "intensity": "medium",
            },
        )
        assert response.status_code == 200
        assert "7-Day Workout Plan" in response.text
        assert "Nutrition" in response.text


    def test_api_generate_and_feedback():
        response = client.post(
            "/api/generate-workout",
            json={
                "username": "API User",
                "user_id": "API001",
                "age": 21,
                "weight": 62,
                "goal": "cardio fitness",
                "intensity": "low",
            },
        )
        assert response.status_code == 200
        assert "workout_plan" in response.json()

        feedback = client.post(
            "/api/submit-feedback/API001",
            json={
                "user_id": "API001",
                "feedback": "Please include more recovery time.",
            },
        )
        assert feedback.status_code == 200
        assert "updated_plan" in feedback.json()
