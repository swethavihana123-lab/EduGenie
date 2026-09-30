from fastapi import FastAPI, Request, Form
from dotenv import load_dotenv

load_dotenv()
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from qna import answer_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations

app = FastAPI(title="EduGenie - AI Learning Assistant")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.post("/qa")
async def qa(text: str = Form(...)):
    return {"result": answer_question(text)}


@app.post("/explain")
async def explain(text: str = Form(...)):
    return {"result": explain_topic(text)}


@app.post("/quiz")
async def quiz(text: str = Form(...)):
    return {"result": generate_quiz(text)}


@app.post("/summarize")
async def summarize(text: str = Form(...)):
    return {"result": summarize_text(text)}


@app.post("/learn/recommendations")
async def recommendations(text: str = Form(...)):
    return {"result": get_learning_recommendations(text)}


