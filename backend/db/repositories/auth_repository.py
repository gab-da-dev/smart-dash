from __future__ import annotations
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from datetime import date
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import select
from litestar.contrib.sqlalchemy.repository import SQLAlchemyAsyncRepository
from litestar.handlers.http_handlers.decorators import delete, patch, post
from litestar.params import Parameter
from litestar.repository.filters import LimitOffset
from passlib.context import CryptContext

from db.models.models import User

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession



class AuthRepository(SQLAlchemyAsyncRepository[User]):
    """Auth repository."""

    model_type = User


async def provide_auth_repo(db_session: AsyncSession) -> AuthRepository:
    """This provides the default auths repository."""
    return AuthRepository(session=db_session)


# we can optionally override the default `select` used for the repository to pass in
# specific SQL options such as join details
async def provide_auth_details_repo(db_session: AsyncSession) -> AuthRepository:
    """This provides a simple example demonstrating how to override the join options
    for the repository."""
    return AuthRepository(
        statement=select(User),
        session=db_session,
    )

