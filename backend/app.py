from datetime import date
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Float, ForeignKey, Text, Uuid, select
from sqlalchemy.orm import Mapped, mapped_column, relationship

from litestar import Litestar, get
from litestar.contrib.sqlalchemy.base import UUIDAuditBase, UUIDBase
from litestar.contrib.sqlalchemy.plugins import AsyncSessionConfig, SQLAlchemyAsyncConfig, SQLAlchemyInitPlugin
from controllers.ingredient_controller import IngredientController
from controllers.product_ingredient_controller import ProductIngredientController
from controllers.store_profile_controller import StoreProfileController
from controllers.product__category_controller import ProductCategoryController
from db.repositories.product_repository import provide_limit_offset_pagination
from litestar.di import Provide
from controllers.product_controller import ProductController
from controllers.order_controller import OrderController

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
    

session_config = AsyncSessionConfig(expire_on_commit=False)
sqlalchemy_config = SQLAlchemyAsyncConfig(
    connection_string="postgresql+asyncpg://developer:user@localhost:5600/smart_dash", session_config=session_config
)  # Create 'async_session' dependency.
sqlalchemy_plugin = SQLAlchemyInitPlugin(config=sqlalchemy_config)


async def on_startup() -> None:
    """Initializes the database."""
    async with sqlalchemy_config.get_engine().begin() as conn:
        await conn.run_sync(UUIDBase.metadata.create_all)


app = Litestar(
    debug=True,
    route_handlers=[ProductController,ProductCategoryController,StoreProfileController, OrderController,ProductIngredientController, IngredientController],
    on_startup=[on_startup],
    plugins=[SQLAlchemyInitPlugin(config=sqlalchemy_config)],
    dependencies={"limit_offset": Provide(provide_limit_offset_pagination)},
)