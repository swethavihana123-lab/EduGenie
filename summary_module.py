import os

try:
    from google import genai
except ImportError:
    genai = None


def summarize_text(text: str):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key or not genai:
        return (
            "Gemini API is not configured. Add GEMINI_API_KEY to .env "
            "to summarize the passage."
        )

    try:
        client = genai.Client(api_key=api_key)

        prompt = f"""
Summarize the following educational passage.
Keep the key points, remove unnecessary repetition,
and use simple language.

Passage:
{text}
"""

        response = client.models.generate_content(
            model=os.getenv("GEMINI_MODEL", "gemini-3.8-flash"),
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Summary error: {e}"

