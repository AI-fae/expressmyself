from pydantic import BaseModel
from datetime import datetime
from typing import List

class Articles(BaseModel):
    title: str
    body: str
    created_at: str = str(datetime.now())

class ArticleCreator(BaseModel):
    username:str
    
    class Config():
        orm_mode = True

class DisplayArticle(BaseModel):
    title:str
    body:str
    owner: ArticleCreator

    class Config():
        orm_mode = True