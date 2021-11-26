from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def hash_password(password):
    """encrypts the user password into non_human readable hash.

    The hashing is a one_way. so, once a password is hashed,
    it can't be recovered in plain text again

    Args:
        password(str):  registration password inputed by user.
        
    Returns:
        hashedPassword: A hashed version of the received password
    """
    hashedPassword = pwd_cxt.hash(password)
    return hashedPassword

async def verify_password(plain_password: str, hashed_password: str):

    """verifies a user's password upon login.

    compares the plain text password provided by the user 
    with the hashed password stored in the database.

    Args:
        plain_password(str):  login password inputed by user.
        hashed_password (str): hashed password retrieved from user info. 
        
    Returns:
        a boolean. True if plain and hashed password match 
        and false if they don't match.
    """

    return pwd_cxt.verify(plain_password, hashed_password)