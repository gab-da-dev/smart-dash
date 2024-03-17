from uuid import UUID

from pydantic import BaseModel as _BaseModel

from schemas.base import BaseSchema


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


class ProductCategoryUpdate(BaseSchema):
    name: str
    active: bool
    description: str


class ProductCategoryCreate(BaseModel):
    class Config:
        orm_mode = True

    name: str
    active: bool
    description: str

