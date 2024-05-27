from uuid import UUID

from pydantic import BaseModel as _BaseModel

from schemas.base import BaseSchema


class BaseModel(_BaseModel):
    """Extend Pydantic's BaseModel to enable ORM mode"""

    model_config = {"from_attributes": True}

class ProductIngredientCreate(BaseModel):
    # product_id: UUID
    ingredient_id: UUID


class Login(BaseModel):
    email: str
    password: str


class LoginRead(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    email: str

class RegisterRequest(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    email: str
    password: str

class JWTUserPayload(BaseModel):
    id: UUID

    class Config:
        orm_mode = True

    @classmethod
    def from_user(cls, user):
        return cls(id=str(user.id), email=user.email)