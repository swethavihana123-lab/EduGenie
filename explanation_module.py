import os

try:
    from google import genai
except ImportError:
    genai = None


def explain_topic(topic: str):
    api_key = os.getenv("GEMINI_API_KEY")

    if api_key and genai:
        try:
            client = genai.Client(api_key=api_key)
            prompt = f"""
Explain the following educational topic for a beginner.
Use simple words, short sections, examples, and bullet points.
Topic: {topic}
"""
            response = client.models.generate_content(
                model=os.getenv("GEMINI_MODEL", "gemini-3.8-flash"),
                contents=prompt
            )
            return response.text
        except Exception as e:
            return f"Gemini API error: {e}"

    return (
        f"Simple explanation for '{topic}':\n\n"
        "Gemini API is not configured. Add your GEMINI_API_KEY "
        "to the .env file to generate an AI explanation."
    )

