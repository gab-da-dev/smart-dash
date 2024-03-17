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
    quantity: int
    price: float
    note: str
class OrderRead(BaseModel):
    class Config:
        orm_mode = True

    id: UUID
    address: str 
    collect_status: bool 
    delivery_status: str 
    delivery_cost: str 
    distance: str 
    driver_latitude: str 
    driver_longitude: str 
    delivery_latitude: str 
    delivery_longitude: str 
    order_type: OrderType 
    food_rating: Rating 
    food_comment: str 
    driver_rating: Rating 
    driver_comment: str 
    status: bool 
    skip_comment: bool 
    user_id: UUID 


class OrderUpdate(BaseSchema):
    collect_status: bool 
    delivery_status: str 
    delivery_cost: str 
    distance: str 
    driver_latitude: str 
    driver_longitude: str 
    delivery_latitude: str 
    delivery_longitude: str 
    food_rating: Rating 
    food_comment: str 
    driver_rating: Rating 
    driver_comment: str 
    status: bool 
    skip_comment: bool 
    user_id: UUID 


class OrderCreate(BaseModel):
    class Config:
        orm_mode = True

    address: str 
    collect_status: bool 
    delivery_status: str 
    delivery_cost: str 
    distance: str 
    driver_latitude: str 
    driver_longitude: str 
    delivery_latitude: str 
    delivery_longitude: str 
    order_type: OrderType 
    food_rating: Rating 
    food_comment: str 
    driver_rating: Rating 
    driver_comment: str 
    status: bool 
    skip_comment: bool 
    user_id: UUID 

