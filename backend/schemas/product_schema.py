from uuid import UUID

from pydantic import BaseModel as _BaseModel

from schemas.base import BaseSchema


class BaseModel(_BaseModel):
    """Extend Pydantic's BaseModel to enable ORM mode"""

    model_config = {"from_attributes": True}

class ProductIngredient(BaseModel):
    name: str
    active: bool
    price: str
    
class ProductRead(BaseModel):
    class Config:
        orm_mode = True

    id: UUID
    active: bool
    name: str
    description: str
    image: str
    product_category_id: str | None
    price: float
    prep_time: str
    product_ingredients:list[ProductIngredient]


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

