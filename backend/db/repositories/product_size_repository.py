from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import select
from litestar.contrib.sqlalchemy.repository import SQLAlchemyAsyncRepository
from litestar.params import Parameter
from litestar.repository.filters import LimitOffset

from db.models.models import ProductSize

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession



class ProductSizeRepository(SQLAlchemyAsyncRepository[ProductSize]):
    """Product size repository."""

    model_type = ProductSize


async def provide_product_size_repo(db_session: AsyncSession) -> ProductSizeRepository:
    """This provides the default Products size repository."""
    return ProductSizeRepository(session=db_session)


# we can optionally override the default `select` used for the repository to pass in
# specific SQL options such as join details
async def provide_product_size_details_repo(db_session: AsyncSession) -> ProductSizeRepository:
    """This provides a simple example demonstrating how to override the join options
    for the repository."""
    return ProductSizeRepository(
        statement=select(ProductSize),
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
