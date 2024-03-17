from typing import TypeVar

from pydantic import BaseModel

class BaseSchema(BaseModel):
    """Base schema model for input deserialisation, validation and output serialisation."""

    class Config:
        orm_mode = True
        use_enum_values = True
