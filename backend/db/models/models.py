from sqlalchemy import Boolean, DateTime, Enum, Float, ForeignKey, Integer, Text, Uuid
from sqlalchemy.orm import Load, Mapped, joinedload, load_only, mapped_column, noload, relationship, selectinload
from uuid import UUID

from sqlalchemy import Float, ForeignKey, Text, Uuid, select
from litestar.contrib.sqlalchemy.base import UUIDAuditBase, UUIDBase


class Product(UUIDAuditBase):

    __tablename__ = "product"

    title: Mapped[str] = mapped_column(Text(), nullable=False)
    active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    description: Mapped[str] = mapped_column(Text(), nullable=False)
    image: Mapped[str] = mapped_column(Text(), nullable=False)
    product_category_id: Mapped[UUID] = mapped_column(Uuid(),ForeignKey("product_category.id"), nullable=True)
    price:  Mapped[float] = mapped_column(Float(), nullable=False)
    prep_time: Mapped[str] = mapped_column(Text(), nullable=False)
    # size_pricing: Mapped[Author] = relationship(lazy="joined", innerjoin=True, viewonly=True)

class ProductCategory(UUIDAuditBase):

    __tablename__ = "product_category"

    name: Mapped[str]
    active: Mapped[bool] = mapped_column()
    description: Mapped[str] = mapped_column()
    # size_pricing: Mapped[Author] = relationship(lazy="joined", innerjoin=True, viewonly=True)
