from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import select
from litestar.contrib.sqlalchemy.repository import SQLAlchemyAsyncRepository

from db.models.models import OrderProductIngredient

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession



class OrderProductIngredientRepository(SQLAlchemyAsyncRepository[OrderProductIngredient]):
    """Order repository."""

    model_type = OrderProductIngredient


async def provide_order_product_ingredient_repo(db_session: AsyncSession) -> OrderProductIngredientRepository:
    """This provides the default Orders repository."""
    return OrderProductIngredientRepository(session=db_session)


# we can optionally override the default `select` used for the repository to pass in
# specific SQL options such as join details
async def provide_order_product_ingredient_details_repo(db_session: AsyncSession) -> OrderProductIngredientRepository:
    """This provides a simple example demonstrating how to override the join options
    for the repository."""
    return OrderProductIngredientRepository(
        statement=select(OrderProductIngredient),
        session=db_session,
    )

