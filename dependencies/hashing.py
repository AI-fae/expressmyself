from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def hash_password(password):
    hashedPassword = pwd_cxt.hash(password)
    return hashedPassword

async def verify_password(plain_password, hashed_password):
    return pwd_cxt.verify(plain_password, hashed_password)