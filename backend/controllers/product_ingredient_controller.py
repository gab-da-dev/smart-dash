from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, ClassVar
from uuid import UUID

from pydantic import TypeAdapter
from litestar import Litestar, get, put
from litestar.controller import Controller
from litestar.di import Provide
from litestar.handlers.http_handlers.decorators import delete, patch, post
from litestar.pagination import OffsetPagination
from litestar.params import Parameter
from litestar.repository.filters import LimitOffset
from db.repositories.product_ingredient_repository import provide_product_ingredient_details_repo, ProductIngredientRepository, provide_product_ingredients_repo
from schemas.product_schema import ProductIngredientCreate, ProductIngredientRead, ProductIngredientUpdate
from db.models.models import ProductIngredient

from db.repositories.product_repository import provide_products_repo

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession



class ProductIngredientController(Controller):
    path = "/product-ingredient"
    dependencies:ClassVar[dict[str, Provide]] = {"repository": Provide(provide_product_ingredients_repo)}

    tags: ClassVar[list[str]] = ["product_ingredient"]

    @post(path="/")
    async def create_product_ingredient(
        self,
        repository: ProductIngredientRepository,
        data: ProductIngredientCreate,
    ) -> ProductIngredientRead:
        """Create a new product ingredient."""
        obj = await repository.add(
            ProductIngredient(**data.model_dump(exclude_unset=True, exclude_none=True)),

        )
        await repository.session.commit()
        return ProductIngredientRead.model_validate(obj)

        # we override the products_repo to use the version that joins the Books in

    @get(path="/{product_ingredient_id:uuid}")
    async def get_product_ingredient(
        self,
        repository: ProductIngredientRepository,
        product_ingredient_id: UUID = Parameter(
            title="Product ID",
            description="The product to retrieve.",
        ),
    ) -> ProductIngredientRead:
        """Get an existing product."""
        
        obj = await repository.get(product_ingredient_id)
        # obj = await products_repo.get_one_or_none(product_ingredient_id)
        return ProductIngredientRead.model_validate(obj)
        
    # TODO: check how to put in a not found exception
    
    @get("/all")
    async def list_all_product_ingredients(
        self,
        repository: ProductIngredientRepository,
        limit_offset: LimitOffset,
        )-> OffsetPagination[ProductIngredient]:
        """Get list of products."""
        results, total = await repository.list_and_count(limit_offset)
        type_adapter = TypeAdapter(list[ProductIngredientRead])
        return OffsetPagination[ProductIngredientRead](
            items=type_adapter.validate_python(results),
            total=total,
            limit=limit_offset.limit,
            offset=limit_offset.offset,
        )
    
    @put(path="/{product_ingredient_id:uuid}")
    async def update_product_ingredient(
        self,
        repository: ProductIngredientRepository,
        data: ProductIngredientUpdate,
        product_ingredient_id: UUID = Parameter(
            title="Product ID",
            description="The product to update.",
        ),
    ) -> ProductIngredientRead:
        """Update an product."""

        raw_obj = data.model_dump(exclude_unset=True, exclude_none=True)
        raw_obj.update({"id": product_ingredient_id})
        obj = await repository.update(ProductIngredient(**raw_obj))
        await repository.session.commit()
        return ProductIngredientRead.from_orm(obj)


    @delete(path="/{product_ingredient_id:uuid}")
    async def delete_product_ingredient(
        self,
        repository: ProductIngredientRepository,
        product_ingredient_id: UUID = Parameter(
            title="Product ID",
            description="The product to delete.",
        ),
    ) -> None:
        """Delete a product from the system."""

        _ = await repository.delete(product_ingredient_id)
        await repository.session.commit()


