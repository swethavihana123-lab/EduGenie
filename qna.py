import os

try:
    from google import genai
except ImportError:
    genai = None


def _gemini(prompt: str):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key or genai is None:
        return None

    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model=os.getenv("GEMINI_MODEL", "gemini-3.8-flash"),
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Gemini API error: {e}"


def answer_question(question: str):
    prompt = f"""
You are EduGenie, an educational assistant.
Answer the student's question accurately and concisely.
Use simple language and explain important terms when needed.

Question:
{question}
"""
    result = _gemini(prompt)

    if result:
        return result

    return (
        "Gemini API is not configured yet. Please add GEMINI_API_KEY "
        "to the .env file. Your question was: " + question
    )

