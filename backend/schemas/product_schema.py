from uuid import UUID

from pydantic import BaseModel as _BaseModel

from schemas.product_size_schema import ProductSizeRead
from schemas.base import BaseSchema
from litestar.datastructures import UploadFile
class BaseModel(_BaseModel):
    """Extend Pydantic's BaseModel to enable ORM mode"""

    model_config = {"from_attributes": True}

class ProductIngredientCreate(BaseModel):
    # product_id: UUID
    ingredient_id: UUID


class IngredientRead(BaseModel):
    id: UUID
    name: str
    active: bool
    price: float

class ProductIngredientRead(BaseModel):
    id: UUID
    ingredient:IngredientRead


class ProductIngredientUpdate(BaseModel):
    product_id: str
    active: bool
    price: str
    
class ProductRead(BaseModel):
    class Config:
        orm_mode = True

    id: UUID
    name: str
    active: bool
    description: str
    image: str
    product_category_id: UUID
    price: float
    prep_time: str


class ProductReadFull(BaseModel):
    class Config:
        orm_mode = True

    id: UUID
    name: str
    active: bool
    description: str
    image: str
    product_category_id: UUID
    price: float
    prep_time: str
    product_ingredients:list[ProductIngredientRead]
    product_size:list[ProductSizeRead]


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
        arbitrary_types_allowed = True

    name: str
    active: bool
    description: str
    image: UploadFile | None
    product_category_id: str
    price: float
    prep_time: str
    ingredients: list[str] | None
