from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash:
    async def bcrypt(password):
        hashedPassword = pwd_cxt.hash(password)
        return hashedPassword