from uuid import UUID

from pydantic import BaseModel

from schemas.base import BaseSchema


class ProductRead(BaseModel):
    class Config:
        orm_mode = True

    id: UUID
    active: bool
    name: str
    description: str
    image: str
    product_category_id: str
    price: float
    prep_time: str


class ProductUpdate(BaseSchema):
    active: bool
    name: str
    description: str
    image: str
    product_category_id: str
    price: float
    prep_time: str


class ProductCreate(BaseModel):
    class Config:
        orm_mode = True

    active: bool
    title: str
    description: str
    image: str
    product_category_id: str
    price: float
    prep_time: str
