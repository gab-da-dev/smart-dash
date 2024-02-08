from datetime import date
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Float, ForeignKey, Text, Uuid, select
from sqlalchemy.orm import Mapped, mapped_column, relationship

from litestar import Litestar, get
from litestar.contrib.sqlalchemy.base import UUIDAuditBase, UUIDBase
from litestar.contrib.sqlalchemy.plugins import AsyncSessionConfig, SQLAlchemyAsyncConfig, SQLAlchemyInitPlugin

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession


# the SQLAlchemy base includes a declarative model for you to use in your models.
# The `Base` class includes a `UUID` based primary key (`id`)
# class Product(UUIDBase):
#     name: Mapped[str]
#     price: Mapped[date]
    # books: Mapped[list["Book"]] = relationship(back_populates="author", lazy="selectin")


# The `AuditBase` class includes the same UUID` based primary key (`id`) and 2
# additional columns: `created_at` and `updated_at`. `created_at` is a timestamp of when the
# record created, and `updated_at` is the last time the record was modified.
class Product(UUIDAuditBase):
    title: Mapped[str] = mapped_column(Text(), nullable=False)
    active: Mapped[bool] = mapped_column()
    description: Mapped[str] = mapped_column(Text(), nullable=False)
    image: Mapped[str] = mapped_column(Text(), nullable=False)
    product_category_id: Mapped[UUID] = mapped_column(Uuid(),ForeignKey("product_category.id"), nullable=True)
    price:  Mapped[float] = mapped_column(Float(), nullable=False)
    prep_time: Mapped[str] = mapped_column(Text(), nullable=False)
    # size_pricing: Mapped[Author] = relationship(lazy="joined", innerjoin=True, viewonly=True)


class ProductCategory(UUIDAuditBase):
    name: Mapped[str]
    active: Mapped[bool] = mapped_column()
    description: Mapped[str] = mapped_column()
    # size_pricing: Mapped[Author] = relationship(lazy="joined", innerjoin=True, viewonly=True)


session_config = AsyncSessionConfig(expire_on_commit=False)
sqlalchemy_config = SQLAlchemyAsyncConfig(
    connection_string="postgresql+asyncpg://developer:user@postgres:5432/smart_dash", session_config=session_config
)  # Create 'async_session' dependency.
sqlalchemy_plugin = SQLAlchemyInitPlugin(config=sqlalchemy_config)


async def on_startup() -> None:
    """Initializes the database."""
    async with sqlalchemy_config.get_engine().begin() as conn:
        await conn.run_sync(UUIDBase.metadata.create_all)


@get(path="/products")
async def get_authors(db_session: "AsyncSession", db_engine: "AsyncEngine") -> list[Product]:
    """Interact with SQLAlchemy engine and session."""
    return list(await db_session.scalars(select(Product)))


app = Litestar(
    route_handlers=[get_authors],
    on_startup=[on_startup],
    plugins=[SQLAlchemyInitPlugin(config=sqlalchemy_config)],
)