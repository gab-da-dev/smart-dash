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

from db.models.models import StoreProfile

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession



class StoreProfileRepository(SQLAlchemyAsyncRepository[StoreProfile]):
    """StoreProfile repository."""

    model_type = StoreProfile


async def provide_store_profile_repo(db_session: AsyncSession) -> StoreProfileRepository:
    """This provides the default StoreProfiles repository."""
    return StoreProfileRepository(session=db_session)


# we can optionally override the default `select` used for the repository to pass in
# specific SQL options such as join details
async def provide_store_profile_details_repo(db_session: AsyncSession) -> StoreProfileRepository:
    """This provides a simple example demonstrating how to override the join options
    for the repository."""
    return StoreProfileRepository(
        statement=select(StoreProfile),
        session=db_session,
    )

