import secrets
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Express Myself"
    API_V1_STR: str = "/api/expressmyself/v1"
    admin_email: str = ""
    SECRET_KEY: str = secrets.token_urlsafe(32)

settings =Settings()