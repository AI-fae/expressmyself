from datetime import datetime, timedelta
from jose import JWTError, jwt
from schemas.user_schema import TokenData

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

async def create_access_token(data: dict):
    """creates authentication token for a user.
    Args:
        data (dict): A key value pair of user infomation to be authenticated

    Returns:
        encoded_jwt: an encoded token used to provide user access
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def verify_token(token: str, credentials_exception):
    """validates access token 
    Args:
        token (str): An OAuth2password bearer obtained from the login url.
        credentials_exception: exception details to be raised if user
             credentails is not valid
    Returns:
        token_data: an object containing user data
    Raises
        HTTP_401_UNAUTHORIZED: invalid credentials
        JWTError: invalid token
    """
    
    try:
        payload =jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
    return token_data
    