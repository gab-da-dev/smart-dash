from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar
from uuid import UUID

from pydantic import TypeAdapter

from sqlalchemy import select

from sqlalchemy.exc import IntegrityError, NoResultFound
from litestar.exceptions import ClientException, NotFoundException
from litestar import Litestar, get, put
from litestar.controller import Controller
from litestar.di import Provide
from litestar.handlers.http_handlers.decorators import delete, patch, post
from litestar.pagination import OffsetPagination
from litestar.params import Parameter
from litestar.repository.filters import LimitOffset
from schemas.auth_schema import Login, LoginRead
from schemas.product_schema import ProductCreate, ProductIngredientCreate, ProductIngredientRead, ProductRead, ProductReadDetail, ProductUpdate
from db.models.models import Product, ProductIngredient, User

from db.repositories.product_repository import ProductRepository, provide_product_details_repo, provide_products_repo
from db.repositories.product_ingredient_repository import provide_product_ingredient_details_repo, ProductIngredientRepository
from db.repositories.auth_repository import provide_auth_details_repo, provide_auth_repo, AuthRepository

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession



class AuthController(Controller):
    path = "/auth"
    dependencies:ClassVar[dict[str, Provide]] = {"repository": Provide(provide_auth_repo)}

    tags: ClassVar[list[str]] = ["auth"]

    @post(path="/login")
    async def login(
        self,
        data: Login,
        repository: AuthRepository
    ) -> User:
        """Create a new product."""
        query = select(User).where(User.email == data.email)

        result = await repository.session.execute(query)
        # print(LoginRead(**result.scalar_one().to_dict()))
        try:
            return result.scalar_one().to_dict(exclude=['password'])

        except NoResultFound as e:
            raise NotFoundException(detail=f"Credentials invalid") from e

