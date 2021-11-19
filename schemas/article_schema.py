from pydantic import BaseModel
from datetime import datetime
from typing import List

class Blog(BaseModel):
    title: str
    body: str
    created_at: str = str(datetime.now())

    class Config():
        orm_mode = True


class User(BaseModel):
    username: str
    email: str
    password: str
    

class DisplayUser(BaseModel):
    username: str
    email: str  

    class Config():
        orm_mode = True


class DisplayBlog(BaseModel):
    title:str
    body:str
    owner_id: DisplayUser

    class Config():
        orm_mode = True