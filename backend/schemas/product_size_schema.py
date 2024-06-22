from uuid import UUID

from pydantic import BaseModel as _BaseModel



class BaseModel(_BaseModel):
    """Extend Pydantic's BaseModel to enable ORM mode"""

    model_config = {"from_attributes": True}


class ProductSizeCreate(BaseModel):
    name: str
    active: bool
    description: str
    price: float

class ProductSizeRead(BaseModel):
    id: UUID
    name: str
    active: bool
    description: str
    price: float


class ProductSizeUpdate(BaseModel):
    name: str
    active: bool
    description: str
    price: float
    
