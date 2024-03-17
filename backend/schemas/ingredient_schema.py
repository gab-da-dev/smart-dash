from uuid import UUID

from pydantic import BaseModel as _BaseModel

from schemas.base import BaseSchema


class BaseModel(_BaseModel):
    """Extend Pydantic's BaseModel to enable ORM mode"""

    model_config = {"from_attributes": True}

class IngredientCreate(BaseModel):
    name: str
    active: bool
    price: str

class IngredientRead(BaseModel):
    id: UUID
    name: str
    active: bool
    price: str


class IngredientUpdate(BaseModel):
    name: str
    active: bool
    price: str
  