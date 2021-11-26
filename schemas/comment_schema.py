from pydantic import BaseModel
from datetime import datetime
from typing import str


class Comment(BaseModel):
    """Describes the request model for adding a new comment to an article."""

    message: str
    username: str
    created_at: str = str(datetime.utcnow())