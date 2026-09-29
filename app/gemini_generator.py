from .config import get_settings


def _demo_plan(username: str, age: int, weight: float, goal: str, intensity: str) -> str:
    level_note = {
        "low": "gentle, beginner-friendly movement",
        "medium": "moderate training with controlled progression",
        "high": "challenging training with careful recovery",
    }[intensity]

    days = [
        ("Day 1", "Full Body", "Bodyweight squat, wall/incline push-up, glute bridge, bird-dog"),
        ("Day 2", "Cardio & Mobility", "Brisk walk, marching, hip mobility, shoulder mobility"),
        ("Day 3", "Upper Body & Core", "Incline push-up, resistance-band row, dead bug, plank"),
        ("Day 4", "Recovery", "Easy walk, gentle stretching and breathing"),
        ("Day 5", "Lower Body", "Squat variation, reverse lunge, calf raise, glute bridge"),
        ("Day 6", "Cardio & Core", "Brisk walk, step-ups, dead bug, side plank"),
        ("Day 7", "Active Recovery", "Easy movement, stretching and rest"),
    ]

    lines = [
        "FITBUDDY 7-DAY WORKOUT PLAN",
        f"Name: {username}",
        f"Goal: {goal}",
        f"Intensity: {intensity}",
        "",
        "This demo plan is generated locally because Gemini is not enabled.",
        "Keep the effort comfortable, use good technique, and take extra rest when needed.",
        "",
    ]
    for day, focus, exercises in days:
        lines.extend([
            f"{day} — {focus}",
            "Warm-up: 5–10 minutes of easy movement.",
            f"Main: {exercises}.",
            f"Approach: {level_note}. Start with a manageable amount and progress gradually.",
            "Cooldown: 5 minutes of easy movement and gentle stretching.",
            "",
        ])
    lines.append("Safety: This is general educational content, not medical advice.")
    return "\n".join(lines)


def generate_workout_gemini(username: str, age: int, weight: float, goal: str, intensity: str) -> str:
    settings = get_settings()
    if settings.demo_mode or not settings.gemini_api_key:
        return _demo_plan(username, age, weight, goal, intensity)

    from google import genai
    from google.genai import types

    client = genai.Client(api_key=settings.gemini_api_key)

    prompt = f"""
Create a safe, practical 7-day general fitness plan for:
Name: {username}
Age: {age}
Weight (kg): {weight}
Fitness goal: {goal}
Preferred intensity: {intensity}

Requirements:
- Give exactly 7 days.
- Each day must have a focus.
- Include warm-up, main workout, and cooldown/recovery.
- Include exercise names and simple sets/reps or time ranges.
- Include at least one recovery/rest-oriented day.
- Do not diagnose, prescribe medication, or provide medical treatment.
- Do not promise weight loss or other guaranteed outcomes.
- Avoid extreme calorie restriction or dangerous exercise.
- If the person has pain, injury, illness, or a medical concern, tell them to consult a qualified professional.
- Keep the response readable in plain text with headings.
"""

    response = client.models.generate_content(
        model=settings.gemini_workout_model,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.6,
            max_output_tokens=2500,
        ),
    )
    return (response.text or "").strip() or _demo_plan(username, age, weight, goal, intensity)
