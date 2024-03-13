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

from db.models.models import Product

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession



class ProductRepository(SQLAlchemyAsyncRepository[Product]):
    """Product repository."""

    model_type = Product


async def provide_products_repo(db_session: AsyncSession) -> ProductRepository:
    """This provides the default Products repository."""
    return ProductRepository(session=db_session)


# we can optionally override the default `select` used for the repository to pass in
# specific SQL options such as join details
async def provide_product_details_repo(db_session: AsyncSession) -> ProductRepository:
    """This provides a simple example demonstrating how to override the join options
    for the repository."""
    return ProductRepository(
        statement=select(Product),
        session=db_session,
    )


def provide_limit_offset_pagination(
    current_page: int = Parameter(ge=1, query="currentPage", default=1, required=False),
    page_size: int = Parameter(
        query="pageSize",
        ge=1,
        default=10,
        required=False,
    ),
) -> LimitOffset:
    """Add offset/limit pagination.

    Return type consumed by `Repository.apply_limit_offset_pagination()`.

    Parameters
    ----------
    current_page : int
        LIMIT to apply to select.
    page_size : int
        OFFSET to apply to select.
    """
    return LimitOffset(page_size, page_size * (current_page - 1))
