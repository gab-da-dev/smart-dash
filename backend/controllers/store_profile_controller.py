from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, ClassVar
from uuid import UUID
from advanced_alchemy import NotFoundError

from pydantic import BaseModel as _BaseModel, TypeAdapter
# from pydantic import TypeAdapter

from litestar import Controller, Litestar, get, put
from litestar.di import Provide
from litestar.handlers.http_handlers.decorators import delete, patch, post
from litestar.pagination import OffsetPagination
from litestar.params import Parameter
from litestar.repository.filters import LimitOffset
from db.models import models
from schemas.store_profile_schema import StoreProfileCreate, StoreProfileRead, StoreProfileUpdate
from db.models.models import Product, StoreProfile

from db.repositories.store_profile_repository import StoreProfileRepository, provide_store_profile_details_repo, provide_store_profile_repo

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession



class StoreProfileController(Controller):
    path = "/store-profile"
    dependencies:ClassVar[dict[str, Provide]] = {"repository": Provide(provide_store_profile_repo)}

    tags: ClassVar[list[str]] = ["store_profile"]

    @post(path="/")
    async def create_store_profile(
        self,
        repository: StoreProfileRepository,
        data: StoreProfileCreate,
    ) -> StoreProfileRead:
        """Create a new product."""
        obj = await repository.add(
            StoreProfile(**data.model_dump(exclude_unset=True, exclude_none=True)),

        )
        await repository.session.commit()
        return StoreProfileRead.model_validate(obj)

        # we override the store_profile_repo to use the version that joins the Books in

    @get(path="/{store_profile_id:uuid}", dependencies={"store_profile_repo": Provide(provide_store_profile_details_repo)})
    async def get_store_profile(
        self,
        store_profile_repo: StoreProfileRepository,
        store_profile_id: UUID = Parameter(
            title="Product ID",
            description="The product to retrieve.",
        ),
    ) -> StoreProfileRead:
        """Get an existing product."""
        
        obj = await store_profile_repo.get(store_profile_id)
        # obj = await store_profile_repo.get_one_or_none(store_profile_id)
        return StoreProfileRead.model_validate(obj)
        
    # TODO: check how to put in a not found exception
    
    @get("/all", exclude_from_auth=True)
    async def list_all_store_profile(
        self,
        repository: StoreProfileRepository,
        limit_offset: LimitOffset,
        )-> OffsetPagination[Product]:
        """Get list of store_profile."""
        results, total = await repository.list_and_count(limit_offset)
        type_adapter = TypeAdapter(list[StoreProfileRead])
        return OffsetPagination[StoreProfileRead](
            items=type_adapter.validate_python(results),
            total=total,
            limit=limit_offset.limit,
            offset=limit_offset.offset,
        )
    
    @put(path="/{store_profile_id:uuid}")
    async def update_store_profile(
        self,
        repository: StoreProfileRepository,
        data: StoreProfileUpdate,
        store_profile_id: UUID = Parameter(
            title="Product ID",
            description="The product to update.",
        ),
    ) -> StoreProfileRead:
        """Update an product."""

        raw_obj = data.model_dump(exclude_unset=True, exclude_none=True)
        raw_obj.update({"id": store_profile_id})
        obj = await repository.update(StoreProfile(**raw_obj))
        await repository.session.commit()
        return StoreProfileRead.from_orm(obj)


    @delete(path="/{store_profile_id:uuid}")
    async def delete_store_profile(
        self,
        repository: StoreProfileRepository,
        store_profile_id: UUID = Parameter(
            title="Product ID",
            description="The product to delete.",
        ),
    ) -> None:
        """Delete a product from the system."""

        _ = await repository.delete(store_profile_id)
        await repository.session.commit()


