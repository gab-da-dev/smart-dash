from datetime import date
from typing import TYPE_CHECKING, cast
from uuid import UUID

from sqlalchemy import Float, ForeignKey, Text, Uuid, select
from sqlalchemy.orm import Mapped, mapped_column, relationship
from litestar.exceptions import NotAuthorizedException
from litestar import Litestar, Request, get
from litestar.contrib.sqlalchemy.base import UUIDAuditBase, UUIDBase
from litestar.contrib.sqlalchemy.plugins import AsyncSessionConfig, SQLAlchemyAsyncConfig, SQLAlchemyInitPlugin
from controllers.auth_controller import AuthController
from controllers.ingredient_controller import IngredientController
from controllers.product_ingredient_controller import ProductIngredientController
from controllers.store_profile_controller import StoreProfileController
from controllers.product_category_controller import ProductCategoryController
from db.repositories.product_repository import provide_limit_offset_pagination
from litestar.di import Provide
from controllers.product_controller import ProductController, serve_product_file
from controllers.order_controller import OrderController
from litestar.openapi import OpenAPIConfig
from litestar.openapi.spec import Components, SecurityScheme, Tag
from litestar.middleware import (
    AbstractAuthenticationMiddleware,
    AuthenticationResult,
)
from litestar.middleware.base import DefineMiddleware
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from litestar.config.cors import CORSConfig

from security.authentication_middleware import JWTAuthenticationMiddleware
if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
    

session_config = AsyncSessionConfig(expire_on_commit=False)
sqlalchemy_config = SQLAlchemyAsyncConfig(
    connection_string="postgresql+asyncpg://developer:user@localhost:5600/smart_dash", session_config=session_config
)  # Create 'async_session' dependency.
sqlalchemy_plugin = SQLAlchemyInitPlugin(config=sqlalchemy_config)


async def init_db() -> None:
    """Initializes the database."""
    async with sqlalchemy_config.get_engine().begin() as conn:
        conn.engine
        await conn.run_sync(UUIDBase.metadata.create_all)


def get_db_connection(app: Litestar) -> "AsyncEngine":
    """Returns the db engine.

    If it doesn't exist, creates it and saves it in on the application state object
    """
    if not getattr(app.state, "engine", None):
        app.state.engine = create_async_engine("postgresql+asyncpg://developer:user@localhost:5600/smart_dash")
    return cast("AsyncEngine", app.state.engine)

SECRET_KEY = 'your_secret_key'
ALGORITHM = 'HS256'


auth_mw = DefineMiddleware(JWTAuthenticationMiddleware, exclude="schema")
app = Litestar(
    cors_config=CORSConfig(allow_origins=["*"]),
    middleware=[auth_mw],
    debug=True,
    route_handlers=[serve_product_file, ProductController,ProductCategoryController,StoreProfileController, OrderController,ProductIngredientController, IngredientController,AuthController],
    on_startup=[init_db, get_db_connection],
    plugins=[SQLAlchemyInitPlugin(config=sqlalchemy_config)],
    dependencies={"limit_offset": Provide(provide_limit_offset_pagination)},
    openapi_config=OpenAPIConfig(
        title="awe",
        version="1.0.0",
        security=[{"BearerToken": []}],
        components=Components(
            security_schemes={
                "BearerToken": SecurityScheme(
                    type="http",
                    scheme="bearer",
                )
            },
        ),
    )
)