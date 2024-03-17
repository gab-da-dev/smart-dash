from uuid import UUID

from pydantic import BaseModel as _BaseModel

from schemas.base import BaseSchema


class BaseModel(_BaseModel):
    """Extend Pydantic's BaseModel to enable ORM mode"""

    model_config = {"from_attributes": True}

class ProductIngredientCreate(BaseModel):
    product_id: UUID
    ingredient_id: UUID

class ProductIngredientRead(BaseModel):
    id: UUID
    name: str
    price: str


class ProductIngredientUpdate(BaseModel):
    product_id: str
    active: bool
    price: str
    
class ProductRead(BaseModel):
    class Config:
        orm_mode = True

    id: UUID
    active: bool
    product_id: str
    description: str
    image: str
    product_category_id: UUID
    price: float
    prep_time: str
    product_ingredients:list[ProductIngredientRead]


class ProductUpdate(BaseSchema):
    active: bool
    product_id: str
    description: str
    image: str
    product_category_id: str
    price: float
    prep_time: str


class ProductCreate(BaseModel):
    class Config:
        orm_mode = True

    active: bool
    product_id: str
    description: str
    image: str
    product_category_id: str
    price: float
    prep_time: str

