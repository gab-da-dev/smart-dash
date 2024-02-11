# from typing import TYPE_CHECKING, Any, Generic, TypeVar

# from src.lib.db.models import DatabaseModelType
# from src.lib.schemas import CreateSchemaType, UpdateSchemaType

# if TYPE_CHECKING:
#     from collections.abc import Sequence
#     from uuid import UUID

#     from sqlalchemy.orm import Load

#     from src.lib.db.repositories.base import BaseRepositoryType


# class Service(Generic[DatabaseModelType, CreateSchemaType, UpdateSchemaType]):
#     """Base class for services integrating to data persistence layers."""

#     model_type: type[DatabaseModelType]

#     def __init__(self, repository: "BaseRepositoryType") -> None:
#         self.repository = repository

#     async def add(self, data: CreateSchemaType) -> DatabaseModelType:
#         return await self.repository.add(self.model_type(**data.dict(exclude_unset=True)))

    
# ServiceType = TypeVar("ServiceType", bound=Service)
