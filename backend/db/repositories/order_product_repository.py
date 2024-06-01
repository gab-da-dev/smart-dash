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

from db.models.models import OrderProduct

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession



class OrderProductRepository(SQLAlchemyAsyncRepository[OrderProduct]):
    """Order repository."""

    model_type = OrderProduct


async def provide_order_product_repo(db_session: AsyncSession) -> OrderProductRepository:
    """This provides the default Orders repository."""
    return OrderProductRepository(session=db_session)


# we can optionally override the default `select` used for the repository to pass in
# specific SQL options such as join details
async def provide_order_product_details_repo(db_session: AsyncSession) -> OrderProductRepository:
    """This provides a simple example demonstrating how to override the join options
    for the repository."""
    return OrderProductRepository(
        statement=select(OrderProduct),
        session=db_session,
    )

