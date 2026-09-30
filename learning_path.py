import os

try:
    from google import genai
except ImportError:
    genai = None


def get_learning_recommendations(topic: str):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key or not genai:
        return (
            "Gemini API is not configured. Add GEMINI_API_KEY to .env "
            "to generate a personalized learning path."
        )

    try:
        client = genai.Client(api_key=api_key)

        prompt = f"""
Create a personalized learning path for: {topic}

Organize it from:
1. Beginner
2. Intermediate
3. Advanced

For each level provide:
- Topics to learn
- Suggested order
- Approximate timeline
- Useful resource types such as videos, articles, or books

Keep it practical and beginner-friendly.
"""

        response = client.models.generate_content(
            model=os.getenv("GEMINI_MODEL", "gemini-3.8-flash"),
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Learning path error: {e}"

