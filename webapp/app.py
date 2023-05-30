from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()
UPLOAD_FOLDER = "images-input"
OUTPUT_FOLDER = "images-output"
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/images-input", StaticFiles(directory=UPLOAD_FOLDER), name="images-input")
app.mount("/images-output", StaticFiles(directory=OUTPUT_FOLDER), name="images-output")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", context={"request": request})