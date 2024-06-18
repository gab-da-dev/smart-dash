
from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel as _BaseModel

from src.enums import OrderType, Rating
from schemas.base import BaseSchema


class BaseModel(_BaseModel):
    """Extend Pydantic's BaseModel to enable ORM mode"""

    model_config = {"from_attributes": True}

class Order(BaseModel):
    class Config:
        orm_mode = True
    
    product_id: UUID
    order_id: UUID
    quantity: int
    price: float
    note: str

class OrderProduct(BaseModel):
    class Config:
        orm_mode = True
    product_id: UUID
    note: str
    additional_ingredients: list[UUID]


class OrderProductCreate(BaseModel):
    class Config:
        orm_mode = True
    
    products: list[Order]


class OrderRead(BaseModel):
    class Config:
        orm_mode = True

    id: UUID
    user_id: UUID 
    address: str 
    collect_status: bool 
    delivery_status: str 
    delivery_cost: str 
    distance: str 
    driver_latitude: str 
    driver_longitude: str 
    delivery_location_latitude: str 
    delivery_location_longitude: str 
    order_type: OrderType 
    food_rating: Rating 
    food_comment: str 
    driver_rating: Rating 
    driver_comment: str 
    status: bool 
    skip_comment: bool 
    created_at: datetime
    order: list[OrderProduct]


class OrderUpdate(BaseSchema):
    user_id: UUID 
    collect_status: bool 
    delivery_status: str 
    delivery_cost: str 
    distance: str 
    driver_latitude: str  
    driver_longitude: str 
    delivery_location_latitude: str 
    delivery_location_longitude: str  
    food_rating: Rating 
    food_comment: str 
    driver_rating: Rating 
    driver_comment: str 
    status: bool 
    skip_comment: bool 


class OrderCreate(BaseModel):
    class Config:
        orm_mode = True

    user_id: UUID 
    delivery_cost: float 
    distance: float 
    status: bool
    address: str
    delivery_location_latitude: str 
    delivery_location_longitude: str  
    collect_status: bool | None
    delivery_status: str | None
    driver_latitude: str | None
    driver_longitude: str | None 
    food_rating: Rating  | None
    food_comment: str | None 
    driver_rating: Rating | None
    driver_comment: str | None 
    skip_comment: bool | None
    order: list[OrderProduct]

