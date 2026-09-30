# EduGenie - Google Gemini Powered Learning Assistant

EduGenie is a lightweight AI educational assistant built with FastAPI,
HTML/CSS and Google Gemini.

## Features

- Question & Answer
- Simple topic explanation
- 3-question MCQ quiz generation
- Text summarization
- Personalized learning recommendations

## Project Structure

EduGenie/
- main.py
- explanation_module.py
- qna.py
- quiz_module.py
- summary_module.py
- learning_path.py
- templates/index.html
- static/style.css
- requirements.txt
- .env.example

## Setup on Windows

1. Install Python 3.10 or newer.
2. Open PowerShell inside the EduGenie folder.
3. Create a virtual environment:

python -m venv venv

4. Activate it:

venv\\Scripts\\activate

5. Install dependencies:

pip install -r requirements.txt

6. Create a file named `.env`.

7. Copy the contents of `.env.example` into `.env`.

8. Replace the API key:

GEMINI_API_KEY=your_actual_key

9. Start the server:

uvicorn main:app --reload

10. Open:

http://127.0.0.1:8000

## API Endpoints

POST /qa
POST /explain
POST /quiz
POST /summarize
POST /learn/recommendations

GET /

The API uses Gemini when GEMINI_API_KEY is configured.
