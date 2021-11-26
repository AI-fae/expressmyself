from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class User(BaseModel):
    """Describes the request model for creating a new user profile."""
    username: str
    email: str
    password: str

class UsersBlog(BaseModel):
    """Describes the response model for fetching an article object."""
    title: str
    body: str
    created_at: str = str(datetime.now())
    
    class Config():
        orm_mode = True

class DisplayUser(BaseModel):
    """Describes the response model for adding/fetching a user profile."""

    username: str
    email: str  
    articles: List[UsersBlog] = None

    class Config():
        orm_mode = True

class Login(BaseModel):
    """Describes the request model for user login."""
    
    email:str
    password:str

class Token(BaseModel):
    """Describes the response model getting an access token."""

    access_token: str
    token_type: str

    class Config():
        orm_mode = True


class TokenData(BaseModel):
    """Describes the type of token data required to authenticate a user"""

    email: Optional[str] = None

    class Config():
        orm_mode = True
