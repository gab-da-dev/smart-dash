from uuid import UUID

from pydantic import BaseModel as _BaseModel

from schemas.product_schema import ProductReadFull
from schemas.base import BaseSchema
from litestar.datastructures import UploadFile

class BaseModel(_BaseModel):
    """Extend Pydantic's BaseModel to enable ORM mode"""

    model_config = {"from_attributes": True}

class ProductCategoryIngredient(BaseModel):
    name: str
    active: bool
    description: str
    
class ProductCategoryRead(BaseModel):
    class Config:
        orm_mode = True

    id: UUID
    name: str
    active: bool
    description: str
    image: str

class ProductCategoryFullRead(BaseModel):
    class Config:
        orm_mode = True

    id: UUID
    name: str
    image: str
    active: bool
    description: str
    products: list[ProductReadFull]


class ProductCategoryUpdate(BaseSchema):
    name: str
    active: bool
    description: str


class ProductCategoryCreate(BaseModel):
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

    name: str
    active: bool
    description: str
    image: UploadFile | None

