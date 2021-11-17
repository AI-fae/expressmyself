from typing import Any
from pydantic import BaseModel

class Register(BaseModel):
    fullname: str
    email: str
    password: Any
    username: str
    

class Login(BaseModel):
    password: Any
    email: str