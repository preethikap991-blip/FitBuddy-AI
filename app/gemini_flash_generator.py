from .config import get_settings


def _demo_tip(goal: str) -> str:
    return (
        f"For your {goal} goal, focus on regular meals, enough water, varied nutritious foods, "
        "and adequate sleep. Avoid extreme dieting. If you have medical or dietary needs, "
        "ask a qualified health professional for individual guidance."
    )


def generate_nutrition_tip_with_flash(goal: str) -> str:
    settings = get_settings()
    if settings.demo_mode or not settings.gemini_api_key:
        return _demo_tip(goal)

    from google import genai
    from google.genai import types

    client = genai.Client(api_key=settings.gemini_api_key)
    prompt = f"""
Give one concise nutrition or recovery tip for a person whose general fitness goal is: {goal}.
Keep it practical, non-medical, and suitable for a general audience.
Do not prescribe supplements or extreme diets. Mention professional advice when individualized
medical or dietary guidance would be needed. Maximum 80 words.
"""
    response = client.models.generate_content(
        model=settings.gemini_tip_model,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.4,
            max_output_tokens=180,
        ),
    )
    return (response.text or "").strip() or _demo_tip(goal)
