from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, status, Depends
from .token import verify_token
from sqlalchemy.orm import Session
from db import models, db_setup


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(db_setup.get_db)):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token_data = await verify_token(token, credentials_exception)
    user = db.query(models.User).filter(models.User.email == token_data.email)
    return user