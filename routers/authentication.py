from fastapi import APIRouter, Depends, status, HTTPException
from schemas.user_schema import Token
from sqlalchemy.orm import Session
from db import db_setup, models
from dependencies import token, hashing
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.post("/login", response_model=Token)
async def login(request: OAuth2PasswordRequestForm =Depends(), db: Session = Depends(db_setup.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                    detail=f"Invalid Credentials")
    verifier = await hashing.verify_password(request.password, user.hashed_password)
    if not verifier:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                    detail=f"Invalid Credentials")
    access_token = await token.create_access_token(data={"sub":user.email})
    return {"access_token": access_token, "token_type": "bearer"}