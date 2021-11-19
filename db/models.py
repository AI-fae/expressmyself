from db.db_setup import Base
from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    articles = relationship("Articles", back_populates="owner")
    created_at: str = str(datetime.now())

class Articles(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    creator_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    owner = relationship("User", back_populates="articles")
    created_at: str = str(datetime.now())