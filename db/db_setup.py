from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQULALCHEMY_DATABASE_URL = 'sqlite:///./blog.db'

engine =create_engine(SQULALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})


SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

def get_db():
    """
    serves as the interface for interacting with the database
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


