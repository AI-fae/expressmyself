from pydantic import BaseModel
from datetime import datetime

class Articles(BaseModel):
    """Describes the request model for creating new articles."""

    title: str
    body: str
    created_at: str = str(datetime.utcnow())

class ArticleCreator(BaseModel):
    """
    Describes the response model for the creator-article orm relationship.
    """
    username:str
    
    class Config():
        orm_mode = True

class DisplayArticle(BaseModel):
    """Describes the response model for creating/fetching an article."""
    title:str
    body:str
    owner: ArticleCreator

    class Config():
        orm_mode = True