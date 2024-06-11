from sqlalchemy import Boolean, DateTime, Enum, Float, ForeignKey, Integer, Text, UniqueConstraint, Uuid
from sqlalchemy.orm import Load, Mapped, joinedload, load_only, mapped_column, noload, relationship, selectinload
from uuid import UUID

from sqlalchemy import Float, ForeignKey, Text, Uuid, select
from litestar.contrib.sqlalchemy.base import UUIDAuditBase, UUIDBase

from src.enums import DeliveryStatus, OrderType, Rating


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
    #relationship
    product_ingredients: Mapped[list["ProductIngredient"]] = relationship(lazy="selectin")
    # order: Mapped[list["OrderProduct"]] = relationship(lazy="selectin")

class ProductIngredient(UUIDAuditBase):

    __tablename__ = "product_ingredients"

    product_id: Mapped[UUID] = mapped_column(Uuid(),ForeignKey("product.id"), nullable=True)
    ingredient_id: Mapped[UUID] = mapped_column(Uuid(), ForeignKey("ingredient.id"), nullable=True)

    ingredient: Mapped["Ingredient"] = relationship(lazy="selectin")

__table_args__ = (
        UniqueConstraint('product_id', 'ingredient_id'),
    )
class Ingredient(UUIDAuditBase):

    __tablename__ = "ingredient"

    name: Mapped[str] = mapped_column(Text(), nullable=False)
    price: Mapped[float] = mapped_column(Float(), nullable=False)
    active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    
    # product: Mapped[Product] = relationship()

class ProductCategory(UUIDAuditBase):

    __tablename__ = "product_category"

    name: Mapped[str] = mapped_column(Text(), nullable=False)
    active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    description: Mapped[str] = mapped_column(Text(), nullable=False)
    # size_pricing: Mapped[Author] = relationship(lazy="joined", innerjoin=True, viewonly=True)
    products: Mapped[list["Product"]] = relationship(lazy="selectin")


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
    email: Mapped[str] = mapped_column(Text(), nullable=False)
    password: Mapped[str] = mapped_column(Text(), nullable=False)


class Order(UUIDAuditBase):
    __tablename__ = "order"

    address: Mapped[str] = mapped_column(Text(), nullable=True)
    collect_status: Mapped[bool] = mapped_column(Boolean(), nullable=True)
    delivery_status: Mapped[DeliveryStatus] = mapped_column(Enum(DeliveryStatus), nullable=True)
    delivery_cost: Mapped[float] = mapped_column(Float(), nullable=True)
    distance: Mapped[float] = mapped_column(Float(), nullable=True)
    driver_latitude: Mapped[str] = mapped_column(Text(), nullable=True)
    driver_longitude: Mapped[str] = mapped_column(Text(), nullable=True)
    delivery_location_latitude: Mapped[str] = mapped_column(Text(), nullable=True)
    delivery_location_longitude: Mapped[str] = mapped_column(Text(), nullable=True)
    order_type: Mapped[OrderType] = mapped_column(Enum(OrderType), nullable=True)
    food_rating: Mapped[Rating] = mapped_column(Enum(Rating), nullable=True)
    food_comment: Mapped[str] = mapped_column(Text(), nullable=True)
    driver_rating: Mapped[Rating] = mapped_column(Enum(Rating), nullable=True)
    driver_comment: Mapped[str] = mapped_column(Text(), nullable=True)
    status: Mapped[bool] = mapped_column(Boolean(), nullable=True)
    skip_comment: Mapped[bool] = mapped_column(Boolean(), nullable=True)
    user_id: Mapped[UUID] = mapped_column(Uuid(), ForeignKey("user.id"))

    #relationship
    order: Mapped[list["OrderProduct"]] = relationship(lazy="selectin")


class OrderProduct(UUIDAuditBase):

    __tablename__ = "order_product"

    order_id: Mapped[UUID] = mapped_column(Uuid(), ForeignKey("order.id"))
    product_id: Mapped[UUID] = mapped_column(Uuid(), ForeignKey("product.id"))
    note: Mapped[str] = mapped_column(Text(), nullable=True)
    quantity: Mapped[int] = mapped_column(Integer(),default=1)
    price: Mapped[float] = mapped_column(Float(), nullable=False)
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