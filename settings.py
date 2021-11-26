import secrets
from pydantic import BaseSettings

class Settings(BaseSettings):

    """Class to hold application config values"""

    app_name: str = "ExpressMyself"
    API_V1_STR: str = "/api/v1"
    admin_email: str = ""
    SECRET_KEY: str = secrets.token_urlsafe(32)

settings =Settings()
