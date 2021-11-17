from pydantic import BaseModel
from datetime import datetime

class Blog(BaseModel):
    title: str
    body: str
    created_at: str = str(datetime.now())


class DisplayBlog(Blog):
    class Config():
        orm_mode = True