from fastapi import APIRouter, Depends, HTTPException, status
from schemas import user_schema
from db import models
from sqlalchemy.orm import Session
from db.db_setup import get_db
from dependencies.hashing import hash_password

router = APIRouter()

@router.post("/user", response_model=user_schema.DisplayUser)
async def create_user(request:user_schema.User, db: Session = Depends(get_db)):
    name = request.username.capitalize()
    user = models.User(
        username=name, email=request.email,
        hashed_password=await hash_password(request.password)
    )
    db.add(user)
    db.commit() 
    db.refresh(user)
    return user

@router.get("/user/{username}", response_model=user_schema.DisplayUser)
def get_user(username, db: Session = Depends(get_db)):
    name = username.capitalize()
    user = db.query(models.User).filter(models.User.username == name)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                    detail=f"invalid username")
    return user.first()



