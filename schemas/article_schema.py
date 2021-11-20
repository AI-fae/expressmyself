from pydantic import BaseModel
from datetime import datetime
from typing import List

class Blog(BaseModel):
    title: str
    body: str
    created_at: str = str(datetime.now())

class BlogCreator(BaseModel):
    username:str
    
    class Config():
        orm_mode = True

class DisplayBlog(BaseModel):
    title:str
    body:str
    owner: BlogCreator

    class Config():
        orm_mode = True