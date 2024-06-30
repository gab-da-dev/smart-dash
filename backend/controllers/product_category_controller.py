from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, ClassVar
from uuid import UUID, uuid4

from pydantic import TypeAdapter
# from pydantic import TypeAdapter
from litestar import get, put
from litestar.controller import Controller
from litestar.di import Provide
from litestar.handlers.http_handlers.decorators import delete, post
from litestar.pagination import OffsetPagination
from litestar.params import Parameter
from litestar.repository.filters import LimitOffset
from schemas.product_category_schema import ProductCategoryCreate, ProductCategoryFullRead, ProductCategoryRead, ProductCategoryUpdate
from db.models.models import Product, ProductCategory
from litestar.enums import RequestEncodingType
from litestar.params import Body
from db.repositories.product_category_repository import ProductCategoryRepository, provide_product_category_details_repo, provide_product_categories_repo

if TYPE_CHECKING:
    pass

UPLOAD_DIRECTORY = Path("uploads")
UPLOAD_DIRECTORY.mkdir(exist_ok=True)

class ProductCategoryController(Controller):
    path = "/product-category"
    dependencies:ClassVar[dict[str, Provide]] = {"repository": Provide(provide_product_categories_repo)}

    tags: ClassVar[list[str]] = ["product_category"]

    @post(path="/", exclude_from_auth=True)
    async def create_product_category(
        self,
        repository: ProductCategoryRepository,
        data: ProductCategoryCreate = Body(media_type=RequestEncodingType.MULTI_PART),
    ) -> ProductCategoryRead:
        """Create a new product."""
        file_extension = Path(data.image.filename).suffix
        random_filename = f"{uuid4()}{file_extension}"
        file_location = UPLOAD_DIRECTORY / random_filename
        with open(file_location, "wb") as f:
            f.write(await data.image.read())
            obj = await repository.add(
                ProductCategory(image=random_filename, **data.model_dump(exclude_unset=True, exclude_none=True, exclude=['image'])),

            )
        
        await repository.session.commit()
        return ProductCategoryRead.model_validate(obj)

        # we override the product_category_repo to use the version that joins the Books in

    @get(path="/{product_id:uuid}", dependencies={"product_category_repo": Provide(provide_product_category_details_repo)})
    async def get_product_category(
        self,
        product_category_repo: ProductCategoryRepository,
        product_id: UUID = Parameter(
            title="Product ID",
            description="The product to retrieve.",
        ),
    ) -> ProductCategoryRead:
        """Get an existing product."""
        
        obj = await product_category_repo.get(product_id)
        # obj = await product_category_repo.get_one_or_none(product_id)
        return ProductCategoryRead.model_validate(obj)
        
    # TODO: check how to put in a not found exception
    
    @get("/all", exclude_from_auth=True)
    async def list_all_product_categories(
        self,
        repository: ProductCategoryRepository,
        limit_offset: LimitOffset,
        )-> OffsetPagination[Product]:
        """Get list of products."""
        results, total = await repository.list_and_count(limit_offset)
        type_adapter = TypeAdapter(list[ProductCategoryRead])
        return OffsetPagination[ProductCategoryRead](
            items=type_adapter.validate_python(results),
            total=total,
            limit=limit_offset.limit,
            offset=limit_offset.offset,
        )
    
    @get("/all-categories-with-products", exclude_from_auth=True)
    async def list_all_categories_with_products(
        self,
        repository: ProductCategoryRepository,
        limit_offset: LimitOffset,
        )-> ProductCategoryFullRead:
        """Get list of products."""
        results, total = await repository.list_and_count(limit_offset)
        type_adapter = TypeAdapter(list[ProductCategoryFullRead])
        return OffsetPagination[ProductCategoryFullRead](
            items=type_adapter.validate_python(results),
            total=total,
            limit=limit_offset.limit,
            offset=limit_offset.offset,
        )
    
    @put(path="/{product_category_id:uuid}")
    async def update_product_category(
        self,
        repository: ProductCategoryRepository,
        data: ProductCategoryUpdate,
        product_category_id: UUID = Parameter(
            title="Product ID",
            description="The product to update.",
        ),
    ) -> ProductCategoryRead:
        """Update an product."""

        raw_obj = data.model_dump(exclude_unset=True, exclude_none=True)
        raw_obj.update({"id": product_category_id})
        obj = await repository.update(ProductCategory(**raw_obj))
        await repository.session.commit()
        return ProductCategoryRead.from_orm(obj)


    @delete(path="/{product_category_id:uuid}")
    async def delete_product_category(
        self,
        repository: ProductCategoryRepository,
        product_category_id: UUID = Parameter(
            title="Product ID",
            description="The product to delete.",
        ),
    ) -> None:
        """Delete a product from the system."""

        _ = await repository.delete(product_category_id)
        await repository.session.commit()


