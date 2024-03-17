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

from db.models.models import Order

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession



class OrderRepository(SQLAlchemyAsyncRepository[Order]):
    """Order repository."""

    model_type = Order


async def provide_order_repo(db_session: AsyncSession) -> OrderRepository:
    """This provides the default Orders repository."""
    return OrderRepository(session=db_session)


# we can optionally override the default `select` used for the repository to pass in
# specific SQL options such as join details
async def provide_order_details_repo(db_session: AsyncSession) -> OrderRepository:
    """This provides a simple example demonstrating how to override the join options
    for the repository."""
    return OrderRepository(
        statement=select(Order),
        session=db_session,
    )

