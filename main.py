import os
from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.encoders import jsonable_encoder
from fastapi.login import LoginManager
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from db import engine, DBContext
import models

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


def get_DB():
    with DBContext() as db:
        yield db


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "Home"})

 
@app.get("/tasks")
def get_tasks(db: Session = Depends(get_DB)):
    return jsonable_encoder(db.query(models.Task).first())


@app.get("/login")
def get_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "title": "Login"})


os.urandom(24).hex()