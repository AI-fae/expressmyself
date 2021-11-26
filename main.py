from fastapi import FastAPI
from sqlalchemy import engine
from routers import articles, users, comments
from db import models
from db.db_setup import engine
from settings import settings

app = FastAPI(
    title=settings.app_name, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

models.Base.metadata.create_all(engine)


@app.get("/")
def homepage():
    welcome_note = "Welcome to ExpressMyself API application\
        Kindly proceed to /docs to explore our easy to use API endpoints"
    
    return welcome_note


app.include_router(
    articles.router, prefix=settings.API_V1_STR, tags= ["Articles"]
    ) # include urls from articles.py

app.include_router(
    users.router, prefix=settings.API_V1_STR, tags= ["User"]
    ) # include urls from users.py

app.include_router(
    comments.router, prefix=settings.API_V1_STR, tags= ["Comments"]
    ) # include urls from comments.py

