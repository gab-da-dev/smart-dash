from datetime import datetime, timedelta
from uuid import UUID

from jose import JWTError, jwt
from pydantic import UUID4, BaseModel

# from app.config import settings
from litestar.exceptions import NotAuthorizedException


DEFAULT_TIME_DELTA = timedelta(days=1)
ALGORITHM = "HS256"

SECRET_KEY = 'your_very_secret_key'
ALGORITHM = 'HS256'

class Token(BaseModel):
    exp: datetime
    iat: datetime
    sub: str

def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload if 'exp' in payload and payload['exp'] >= datetime.utcnow().timestamp() else None
    except jwt.PyJWTError:
        return None
    

def decode_jwt_token(encoded_token: str) -> Token:
    """Helper function that decodes a jwt token and returns the value stored under the ``sub`` key
    
    If the token is invalid or expired (i.e. the value stored under the exp key is in the past) an exception is raised
    """
    token = encoded_token.split(" ")[1]
    # payload = decode_access_token(token)
    try:
        payload = jwt.decode(token=token, key=SECRET_KEY, algorithms=[ALGORITHM])
        return Token(**payload)
    except JWTError as e:
        raise NotAuthorizedException("Invalid token") from e


def encode_jwt_token(email: str, expiration: timedelta = DEFAULT_TIME_DELTA) -> str:
    """Helper function that encodes a JWT token with expiration and a given user_id"""
    token = Token(
        exp=datetime.now() + expiration,
        iat=datetime.now(),
        sub=email,
    )
    return jwt.encode(token.dict(), SECRET_KEY, algorithm=ALGORITHM)