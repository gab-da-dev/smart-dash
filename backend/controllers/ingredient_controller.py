from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, ClassVar
from uuid import UUID
from advanced_alchemy import NotFoundError

from pydantic import TypeAdapter

from litestar import Litestar, get, put
from litestar.controller import Controller
from litestar.di import Provide
from litestar.handlers.http_handlers.decorators import delete, post
from litestar.pagination import OffsetPagination
from litestar.params import Parameter
from litestar.repository.filters import LimitOffset
from schemas.ingredient_schema import IngredientCreate, IngredientRead, IngredientUpdate
from db.models.models import Ingredient

from db.repositories.ingredient_repository import IngredientRepository, IngredientRepository, provide_ingredient_details_repo, provide_ingredients_repo

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession



class IngredientController(Controller):
    path = "/ingredient"
    dependencies:ClassVar[dict[str, Provide]] = {"repository": Provide(provide_ingredients_repo)}

    tags: ClassVar[list[str]] = ["ingredient"]

    @post(path="/")
    async def create_ingredient(
        self,
        repository: IngredientRepository,
        data: IngredientCreate,
    ) -> IngredientRead:
        """Create a new ingredient."""
        obj = await repository.add(
            Ingredient(**data.model_dump(exclude_unset=True, exclude_none=True)),

        )
        await repository.session.commit()
        return IngredientRead.model_validate(obj)

        # we override the ingredients_repo to use the version that joins the Books in

    @get(path="/{ingredient_id:uuid}", dependencies={"ingredients_repo": Provide(provide_ingredient_details_repo)})
    async def get_ingredient(
        self,
        ingredients_repo: IngredientRepository,
        ingredient_id: UUID = Parameter(
            title="ingredient ID",
            description="The ingredient to retrieve.",
        ),
    ) -> IngredientRead:
        """Get an existing ingredient."""
        
        obj = await ingredients_repo.get(ingredient_id)
        # obj = await ingredients_repo.get_one_or_none(ingredient_id)
        return IngredientRead.model_validate(obj)
        
    # TODO: check how to put in a not found exception
    
    @get("/all", exclude_from_auth=True)
    async def list_all_ingredients(
        self,
        repository: IngredientRepository,
        limit_offset: LimitOffset,
        )-> OffsetPagination[Ingredient]:
        """Get list of ingredients."""
        results, total = await repository.list_and_count(limit_offset)
        type_adapter = TypeAdapter(list[IngredientRead])
        return OffsetPagination[IngredientRead](
            items=type_adapter.validate_python(results),
            total=total,
            limit=limit_offset.limit,
            offset=limit_offset.offset,
        )
    
    @put(path="/{ingredient_id:uuid}")
    async def update_ingredient(
        self,
        repository: IngredientRepository,
        data: IngredientUpdate,
        ingredient_id: UUID = Parameter(
            title="ingredient ID",
            description="The ingredient to update.",
        ),
    ) -> IngredientRead:
        """Update an ingredient."""

        raw_obj = data.model_dump(exclude_unset=True, exclude_none=True)
        raw_obj.update({"id": ingredient_id})
        obj = await repository.update(Ingredient(**raw_obj))
        await repository.session.commit()
        return IngredientRead.from_orm(obj)


    @delete(path="/{ingredient_id:uuid}")
    async def delete_ingredient(
        self,
        repository: IngredientRepository,
        ingredient_id: UUID = Parameter(
            title="ingredient ID",
            description="The ingredient to delete.",
        ),
    ) -> None:
        """Delete a ingredient from the system."""

        _ = await repository.delete(ingredient_id)
        await repository.session.commit()


