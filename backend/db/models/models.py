from sqlalchemy import Boolean, DateTime, Enum, Float, ForeignKey, Integer, Text, Uuid
from sqlalchemy.orm import Load, Mapped, joinedload, load_only, mapped_column, noload, relationship, selectinload
from uuid import UUID

from sqlalchemy import Float, ForeignKey, Text, Uuid, select
from litestar.contrib.sqlalchemy.base import UUIDAuditBase, UUIDBase


class Product(UUIDAuditBase):

    __tablename__ = "product"

    name: Mapped[str] = mapped_column(Text(), nullable=False)
    active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    description: Mapped[str] = mapped_column(Text(), nullable=False)
    image: Mapped[str] = mapped_column(Text(), nullable=False)
    product_category_id: Mapped[UUID] = mapped_column(Uuid(),ForeignKey("product_category.id"), nullable=True)
    price:  Mapped[float] = mapped_column(Float(), nullable=False)
    prep_time: Mapped[str] = mapped_column(Text(), nullable=False)
    # size_pricing: Mapped[Author] = relationship(lazy="joined", innerjoin=True, viewonly=True)
    # product_ingredients: Mapped[list["ProductIngredient"]] = relationship(lazy="noload")


class ProductIngredient(UUIDAuditBase):

    __tablename__ = "product_ingredients"

    product_id: Mapped[UUID] = mapped_column(Uuid(),ForeignKey("product.id"), nullable=True)
    ingredient_id: Mapped[UUID] = mapped_column(Uuid(), ForeignKey("ingredient.id"), nullable=True)

    # product: Mapped[Product] = relationship()

class Ingredient(UUIDAuditBase):

    __tablename__ = "ingredient"

    name: Mapped[str] = mapped_column(Text(), nullable=False)
    price: Mapped[str] = mapped_column(Text(), nullable=False)
    active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    # product_id: Mapped[UUID] = mapped_column(Uuid(), ForeignKey("product.id"))

    # product: Mapped[Product] = relationship()

class ProductCategory(UUIDAuditBase):

    __tablename__ = "product_category"

    name: Mapped[str] = mapped_column(Text(), nullable=False)
    active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    description: Mapped[str] = mapped_column(Text(), nullable=False)
    # size_pricing: Mapped[Author] = relationship(lazy="joined", innerjoin=True, viewonly=True)


class StoreProfile(UUIDAuditBase):

    __tablename__ = "store_profile"

    name: Mapped[str] = mapped_column(Text(), nullable=False)
    lat: Mapped[str] = mapped_column(Text(), nullable=False)
    lng: Mapped[str] = mapped_column(Text(), nullable=False)
    delivery_cost: Mapped[str] = mapped_column(Text(), nullable=False)
    delivery_limit: Mapped[str] = mapped_column(Text(), nullable=False)
    open_time: Mapped[str] = mapped_column(Text(), nullable=False)
    close_time: Mapped[str] = mapped_column(Text(), nullable=False)
    active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    logo: Mapped[str] = mapped_column(Text(), nullable=False)
    header_image: Mapped[str] = mapped_column(Text(), nullable=False)
    


class User(UUIDAuditBase):

    __tablename__ = "user"

    first_name: Mapped[str] = mapped_column(Text(), nullable=False)
    last_name: Mapped[str] = mapped_column(Text(), nullable=False)
    phone_number: Mapped[str] = mapped_column(Text(), nullable=False)
    password: Mapped[str] = mapped_column(Text(), nullable=False)
    delivery_limit: Mapped[str] = mapped_column(Text(), nullable=False)

    # orders: Mapped[list["Order"]] = relationship(lazy="join")




class Order(UUIDAuditBase):

    __tablename__ = "order"

    address: Mapped[str] = mapped_column(Text(), nullable=False)
    collect_status: Mapped[str] = mapped_column(Text(), nullable=False)
    delivery_status: Mapped[str] = mapped_column(Text(), nullable=False)
    delivery_cost: Mapped[str] = mapped_column(Text(), nullable=False)
    distance: Mapped[str] = mapped_column(Text(), nullable=False)
    driver_latitude: Mapped[str] = mapped_column(Text(), nullable=False)
    driver_longitude: Mapped[str] = mapped_column(Text(), nullable=False)
    latitude: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    longitude: Mapped[str] = mapped_column(Text(), nullable=False)
    order: Mapped[str] = mapped_column(Text(), nullable=False)
    order_type: Mapped[str] = mapped_column(Text(), nullable=False)
    food_rating: Mapped[str] = mapped_column(Text(), nullable=False)
    rating_description: Mapped[str] = mapped_column(Text(), nullable=False)
    driver_rating: Mapped[str] = mapped_column(Text(), nullable=False)
    status: Mapped[str] = mapped_column(Text(), nullable=False)
    skip_comment: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    user_id: Mapped[UUID] = mapped_column(Uuid(), ForeignKey("user.id"))

    # user: Mapped[User] = relationship(back_populates="orders", lazy="selectin")


class Promotion(UUIDAuditBase):

    __tablename__ = "promotion"

    product_id: Mapped[str] = mapped_column(Text(), nullable=False)
    promotion_end: Mapped[str] = mapped_column(Text(), nullable=False)
    promotion_start: Mapped[str] = mapped_column(Boolean(), nullable=False)
    promotion_start: Mapped[str] = mapped_column(Boolean(), nullable=False)
    promotion_price: Mapped[str] = mapped_column(Boolean(), nullable=False)
    active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


class Role(UUIDAuditBase):
    __tablename__ = "role"

    name: Mapped[str] = mapped_column(Text(), nullable=False)
class UserRole(UUIDAuditBase):
    __tablename__ = "user_role"

    user_id: Mapped[UUID] = mapped_column(Uuid(), ForeignKey("user.id"))
    role_id: Mapped[UUID] = mapped_column(Uuid(), ForeignKey("role.id"))