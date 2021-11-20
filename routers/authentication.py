from fastapi import APIRouter, Depends, status, HTTPException
from schemas.user_schema import Login
from sqlalchemy.orm import Session
from db.db_setup import get_db
from db.models import User
from dependencies.hashing import verify_password
from dependencies import token
router = APIRouter()

@router.post("/login")
async def login(request: Login, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                    detail=f"Invalid Credentials")
    verifier = await verify_password(request.password, user.hashed_password)
    if not verifier:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                    detail=f"Invalid password")
    access_token = token.create_access_token(data={"sub":user.email})
    return {"access_token": access_token, "token_type": "bearer"}