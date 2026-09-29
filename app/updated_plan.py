from .config import get_settings


def _demo_updated_plan(original_plan: str, feedback: str) -> str:
    return (
        original_plan
        + "\n\n--- UPDATED USING USER FEEDBACK ---\n"
        + f"Feedback received: {feedback}\n"
        + "Adjustment: Keep the existing plan structure, apply the requested preference "
          "where it is reasonable, and preserve recovery days and safe progression.\n"
    )


def update_workout_plan(original_plan: str, feedback: str, username: str, goal: str, intensity: str) -> str:
    settings = get_settings()
    if settings.demo_mode or not settings.gemini_api_key:
        return _demo_updated_plan(original_plan, feedback)

    from google import genai
    from google.genai import types

    client = genai.Client(api_key=settings.gemini_api_key)
    prompt = f"""
You are revising a general fitness plan.

User: {username}
Goal: {goal}
Intensity: {intensity}

Original plan:
{original_plan}

User feedback:
{feedback}

Return a revised 7-day plan.
Rules:
- Preserve useful parts of the original plan.
- Apply the feedback where reasonable.
- Keep at least one recovery/rest-oriented day.
- Do not provide medical treatment or dangerous exercise.
- Do not promise outcomes.
- Keep the format easy to read.
- If feedback requests something unsafe, replace it with a safer alternative.
"""
    response = client.models.generate_content(
        model=settings.gemini_workout_model,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.6,
            max_output_tokens=2500,
        ),
    )
    return (response.text or "").strip() or _demo_updated_plan(original_plan, feedback)
