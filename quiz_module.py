import json
import os

try:
    from google import genai
except ImportError:
    genai = None


def clean_json_block(text):
    text = text.strip()
    if text.startswith("```"):
        lines = text.splitlines()
        lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        text = "\n".join(lines)
    return text.strip()


def generate_quiz(passage: str):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key or not genai:
        return {
            "message": "Gemini API is not configured. Add GEMINI_API_KEY to .env.",
            "questions": []
        }

    try:
        client = genai.Client(api_key=api_key)

        prompt = f"""
Create exactly 3 multiple-choice questions from the passage below.

Return ONLY valid JSON in this format:
[
  {{
    "question": "Question text",
    "options": ["A", "B", "C", "D"],
    "answer": "Correct option"
  }}
]

Passage:
{passage}
"""

        response = client.models.generate_content(
            model=os.getenv("GEMINI_MODEL", "gemini-3.8-flash"),
            contents=prompt
        )

        cleaned = clean_json_block(response.text)
        questions = json.loads(cleaned)

        return {"questions": questions}

    except Exception as e:
        return {
            "message": f"Quiz generation error: {e}",
            "questions": []
        }

