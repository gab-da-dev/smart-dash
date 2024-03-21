from __future__ import annotations

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
from db.models import models
from schemas.product_schema import ProductCreate, ProductIngredientCreate, ProductIngredientRead, ProductRead, ProductUpdate
from db.models.models import Product, ProductIngredient

from db.repositories.product_repository import ProductRepository, provide_product_details_repo, provide_products_repo
from db.repositories.product_ingredient_repository import provide_product_ingredient_details_repo, provide_product_ingredients_repo, ProductIngredientRepository

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession



class ProductController(Controller):
    path = "/product"
    dependencies:ClassVar[dict[str, Provide]] = {"repository": Provide(provide_products_repo)}

    tags: ClassVar[list[str]] = ["product"]

    @post(path="/")
    async def create_product(
        self,
        repository: ProductRepository,
        data: ProductCreate,
    ) -> ProductRead:
        """Create a new product."""
        obj = await repository.add(
            Product(**data.model_dump(exclude_unset=True, exclude_none=True)),

        )
        await repository.session.commit()
        return ProductRead.model_validate(obj)

        # we override the products_repo to use the version that joins the Books in

    @get(path="/{product_id:uuid}", dependencies={"products_repo": Provide(provide_product_details_repo)})
    async def get_product(
        self,
        products_repo: ProductRepository,
        product_id: UUID = Parameter(
            title="Product ID",
            description="The product to retrieve.",
        ),
    ) -> ProductRead:
        """Get an existing product."""
        
        obj = await products_repo.get(product_id)
        # obj = await products_repo.get_one_or_none(product_id)
        return ProductRead.model_validate(obj)
        
    # TODO: check how to put in a not found exception
    
    @get("/all")
    async def list_all_products(
        self,
        repository: ProductRepository,
        limit_offset: LimitOffset,
        )-> OffsetPagination[Product]:
        """Get list of products."""
        results, total = await repository.list_and_count(limit_offset)
        type_adapter = TypeAdapter(list[ProductRead])
        return OffsetPagination[ProductRead](
            items=type_adapter.validate_python(results),
            total=total,
            limit=limit_offset.limit,
            offset=limit_offset.offset,
        )
    
    @put(path="/{product_id:uuid}")
    async def update_product(
        self,
        repository: ProductRepository,
        data: ProductUpdate,
        product_id: UUID = Parameter(
            title="Product ID",
            description="The product to update.",
        ),
    ) -> ProductRead:
        """Update an product."""

        raw_obj = data.model_dump(exclude_unset=True, exclude_none=True)
        raw_obj.update({"id": product_id})
        obj = await repository.update(Product(**raw_obj))
        await repository.session.commit()
        return ProductRead.from_orm(obj)


    @delete(path="/{product_id:uuid}")
    async def delete_product(
        self,
        repository: ProductRepository,
        product_id: UUID = Parameter(
            title="Product ID",
            description="The product to delete.",
        ),
    ) -> None:
        """Delete a product from the system."""

        _ = await repository.delete(product_id)
        await repository.session.commit()


    @post(path="/{product_id:uuid}/product-ingredient", dependencies={"product_ingredients_repo": Provide(provide_product_ingredients_repo)})
    async def create_product_ingredient(
        self,
        product_id: UUID,
        product_ingredients_repo: ProductIngredientRepository,
        data: ProductIngredientCreate,
    ) -> ProductIngredientRead:
        """Create a new product ingredient."""
        obj = await product_ingredients_repo.add(
            ProductIngredient(product_id=product_id,ingredient_id=data.ingredient_id),

        )
        await product_ingredients_repo.session.commit()
        return ProductIngredientRead.model_validate(obj)