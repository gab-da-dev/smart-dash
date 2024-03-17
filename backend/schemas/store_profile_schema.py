from uuid import UUID

from pydantic import BaseModel as _BaseModel

from schemas.base import BaseSchema


class BaseModel(_BaseModel):
    """Extend Pydantic's BaseModel to enable ORM mode"""

    model_config = {"from_attributes": True}

    
class StoreProfileRead(BaseModel):
    class Config:
        orm_mode = True

    id: UUID
    name: str
    lat: str
    lng: str
    delivery_cost: str
    delivery_limit: str
    open_time: str
    close_time: str
    logo: str
    header_image: str
    active: bool


class StoreProfileUpdate(BaseSchema):
    name: str
    lat: str
    lng: str
    delivery_cost: str
    delivery_limit: str
    open_time: str
    close_time: str
    logo: str
    header_image: str
    active: bool


class StoreProfileCreate(BaseModel):
    class Config:
        orm_mode = True

    name: str
    lat: str
    lng: str
    delivery_cost: str
    delivery_limit: str
    open_time: str
    close_time: str
    logo: str
    header_image: str
    active: bool

