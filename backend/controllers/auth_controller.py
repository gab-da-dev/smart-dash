from __future__ import annotations

from datetime import datetime
from http.client import HTTPException
from typing import TYPE_CHECKING, Any, ClassVar

import jwt
from sqlalchemy import select

from sqlalchemy.exc import NoResultFound
from litestar.exceptions import NotAuthorizedException, NotFoundException
from litestar import Request, get
from litestar.controller import Controller
from litestar.di import Provide
from litestar.handlers.http_handlers.decorators import post
from schemas.auth_schema import Login, RegisterRequest
from db.models.models import User
from security.jwt import Token, encode_jwt_token
from db.repositories.auth_repository import provide_auth_repo, AuthRepository
from passlib.context import CryptContext
if TYPE_CHECKING:
    pass

SECRET_KEY = "your_very_secret_key"
ALGORITHM = "HS256"

class AuthController(Controller):
    path = "/auth"
    dependencies:ClassVar[dict[str, Provide]] = {"repository": Provide(provide_auth_repo)}

    tags: ClassVar[list[str]] = ["auth"]
    
    
    @post("/login", exclude_from_auth=True)
    async def login(self, repository: AuthRepository, data: Login)-> Any:

        SECRET_KEY = "your_very_secret_key"
        ALGORITHM = "HS256" 
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

        def verify_password(plain_password: str, hashed_password: str) -> bool:
            return pwd_context.verify(plain_password, hashed_password)
        
        query = select(User).where(User.email==data.email)
        result = await repository.session.execute(query)

        try:
            user = result.scalar_one()
            # if not user or user.password != "password":  # Replace with actual password validation
            if not user or verify_password(data.password, user.password):  # Replace with actual password validation
                raise NotAuthorizedException()
        except NoResultFound as e:
            raise NotFoundException(detail="not found") from e
        
        # Generate JWT token
        access_token = encode_jwt_token(email=user.email)
        # access_token = jwt.encode({"email": user.email}, SECRET_KEY, algorithm=ALGORITHM)
        return {"access_token": access_token, "token_type": "bearer"}
    
    @get("/")
    def my_route_handler(self, request: Request[User, Token, State]) -> None:
        user = request.user  # correctly typed as User
        auth = request.auth  # correctly typed as Token
        assert isinstance(user, User)
        assert isinstance(auth, Token)

    @post("/register", exclude_from_auth=True)
    async def register(self, repository: AuthRepository, data: RegisterRequest)-> Any:
        
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        
        def hash_password(password: str) -> str:
            return pwd_context.hash(password)

        hashed_password = hash_password(data.password)
        new_user = User(email=data.email, first_name=data.first_name, last_name=data.last_name, password=hashed_password)
        
        await repository.add(
            User(password=hashed_password, **data.model_dump(exclude_unset=True, exclude_none=True, exclude=['password'])),
        
        )
        await repository.session.commit()
        # Optionally, generate JWT token
        access_token = encode_jwt_token(new_user.email)

        return {"access_token": access_token}
        
    @get('/protected')
    async def protected_route(request: Request)->Any:
        user = await get_current_user(request)
        return {"message": f"Hello {user['sub']}"}

def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload if 'exp' in payload and payload['exp'] >= datetime.utcnow().timestamp() else None
    except jwt.PyJWTError:
        return None

async def get_current_user(request: Request):
    token = request.headers.get('Authorization')
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    token = token.split(" ")[1]
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    return payload


