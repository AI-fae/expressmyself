from fastapi import APIRouter
from schemas import user_schema

router = APIRouter()

@router.post("/user")
def create_user(request:user_schema.Register):
    return request