from fastapi import FastAPI
from sqlalchemy import engine
from routers import articles
from db import models
from db.db_setup import engine

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(articles.router)


