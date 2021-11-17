from pydantic import BaseModel
from datetime import datetime
from typing import str


class Comment(BaseModel):
    created_at: str = str(datetime.now())
    message: str
    username: str