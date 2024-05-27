from __future__ import annotations

from http.client import HTTPException
from typing import TYPE_CHECKING, Any, ClassVar
from uuid import UUID


import httpx
import jwt
from sqlalchemy import select

from sqlalchemy.exc import IntegrityError, NoResultFound
from litestar.exceptions import NotAuthorizedException, NotFoundException
from litestar import Litestar, get, put
from litestar.controller import Controller
from litestar.di import Provide
from litestar.handlers.http_handlers.decorators import delete, patch, post
from litestar.pagination import OffsetPagination
from litestar.params import Parameter
from litestar.repository.filters import LimitOffset
from schemas.auth_schema import Login, LoginRead, RegisterRequest
from schemas.product_schema import ProductCreate, ProductIngredientCreate, ProductIngredientRead, ProductRead, ProductReadDetail, ProductUpdate
from db.models.models import Product, ProductIngredient, User

from db.repositories.product_repository import ProductRepository, provide_product_details_repo, provide_products_repo
from db.repositories.product_ingredient_repository import provide_product_ingredient_details_repo, ProductIngredientRepository
from db.repositories.auth_repository import provide_auth_details_repo, provide_auth_repo, AuthRepository
from passlib.context import CryptContext
if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession



class AuthController(Controller):
    path = "/auth"
    dependencies:ClassVar[dict[str, Provide]] = {"repository": Provide(provide_auth_repo)}

    tags: ClassVar[list[str]] = ["auth"]

    @post("/login")
    async def login(self, repository: AuthRepository, data: Login)-> Any:

        SECRET_KEY = "your_very_secret_key"
        ALGORITHM = "HS256" 

        def verify_password(plain_password: str, hashed_password: str) -> bool:
            pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
            return pwd_context.verify(plain_password, hashed_password)
        
        query = select(User).where(User.email==data.email)
        result = await repository.session.execute(query)

        try:
            user = result.scalar_one()
            # if not user or user.password != "password":  # Replace with actual password validation
            if not user or verify_password(data.password, user.password):  # Replace with actual password validation
                raise NotAuthorizedException()
        except NoResultFound as e:
            raise NotFoundException(detail=f"not found") from e
        
        # Generate JWT token
        
        access_token = jwt.encode({"email": user.email}, SECRET_KEY, algorithm=ALGORITHM)
        return {"access_token": access_token}
    

    @post("/register")
    async def register(self, repository: AuthRepository, data: RegisterRequest)-> Any:
        SECRET_KEY = "your_very_secret_key"
        ALGORITHM = "HS256"

        def hash_password(password: str) -> str:
            pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
            return pwd_context.hash(password)

        hashed_password = hash_password(data.password)
        new_user = User(email=data.email, first_name=data.first_name, last_name=data.last_name, password=hashed_password)
        
        await repository.add(
            User(password=hashed_password, **data.model_dump(exclude_unset=True, exclude_none=True, exclude=['password'])),
        await repository.session.commit()
        )
        
        # Optionally, generate JWT token
        payload = {"email": new_user.email, "user_id": new_user.id}
        access_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

        return {"access_token": access_token}
        

