from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class User(BaseModel):
    username: str
    email: str
    password: str

class UsersBlog(BaseModel):
    title: str
    body: str
    created_at: str = str(datetime.now())
    
    class Config():
        orm_mode = True

class DisplayUser(BaseModel):
    username: str
    email: str  
    articles: List[UsersBlog] = None

    class Config():
        orm_mode = True

class Login(BaseModel):
    email:str
    password:str

class Token(BaseModel):
    access_token: str
    token_type: str

    class Config():
        orm_mode = True


class TokenData(BaseModel):
    email: Optional[str] = None

    class Config():
        orm_mode = True
