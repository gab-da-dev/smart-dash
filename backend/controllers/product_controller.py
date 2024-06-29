from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Annotated, ClassVar
from uuid import UUID, uuid4

from pydantic import TypeAdapter

from litestar import Response, get, put
from litestar.controller import Controller
from litestar.di import Provide
from litestar.handlers.http_handlers.decorators import delete, post
from litestar.pagination import OffsetPagination
from litestar.params import Parameter
from litestar.repository.filters import LimitOffset
from db.repositories.product_size_repository import ProductSizeRepository, provide_product_size_repo
from schemas.product_size_schema import ProductSizeCreate, ProductSizeRead
from schemas.product_schema import ProductCreate, ProductIngredientCreate, ProductIngredientRead, ProductRead, ProductReadFull, ProductUpdate
from db.models.models import Product, ProductIngredient, ProductSize
from litestar.enums import RequestEncodingType
from litestar.params import Body
from db.repositories.product_repository import ProductRepository, provide_product_details_repo, provide_products_repo
from db.repositories.product_ingredient_repository import provide_product_ingredients_repo, ProductIngredientRepository

if TYPE_CHECKING:
    pass

UPLOAD_DIRECTORY = Path("uploads")
UPLOAD_DIRECTORY.mkdir(exist_ok=True)

class ProductController(Controller):
    path = "/product"
    dependencies:ClassVar[dict[str, Provide]] = {"repository": Provide(provide_products_repo)}

    tags: ClassVar[list[str]] = ["product"]

    @post(path="/", exclude_from_auth=True, dependencies={"product_ingredients_repo": Provide(provide_product_ingredients_repo)})
    async def create_product(
        self,
        repository: ProductRepository,
        product_ingredients_repo: ProductIngredientRepository,
        data: ProductCreate = Body(media_type=RequestEncodingType.MULTI_PART),
    ) -> ProductRead:
        """Create a new product."""
        file_extension = Path(data.image.filename).suffix
        random_filename = f"{uuid4()}{file_extension}"
        file_location = UPLOAD_DIRECTORY / random_filename
        with open(file_location, "wb") as f:
            f.write(await data.image.read())
            obj = await repository.add(
                Product(image=random_filename, **data.model_dump(exclude_unset=True, exclude_none=True, exclude=['ingredients', 'image'])),

            )
        await repository.session.commit()
         # Extract the product ID
        product_id = obj.id

        # Update ingredients with product ID
        for ingredient_id in data.ingredients:
            await product_ingredients_repo.add(ProductIngredient(product_id=product_id,ingredient_id=ingredient_id))

        # await product_ingredients_repo.session.commit()
        return ProductRead.model_validate(obj)
    
    


    @get(path="/{product_id:uuid}", exclude_from_auth=True, dependencies={"products_repo": Provide(provide_product_details_repo)})
    async def get_product(
        self,
        products_repo: ProductRepository,
        product_id: UUID = Parameter(
            title="Product ID",
            description="The product to retrieve.",
        ),
    ) -> ProductReadFull:
        """Get an existing product."""
        
        obj = await products_repo.get(product_id)
        # obj = await products_repo.get_one_or_none(product_id)
        return ProductReadFull.model_validate(obj)
        
    # TODO: check how to put in a not found exception
    
    @get("/all", exclude_from_auth=True)
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
        return ProductRead.model_validate(obj)


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
    
    @delete(path="/{product_id:uuid}/product-ingredient/{product_ingredient_id:uuid}", dependencies={"product_ingredients_repo": Provide(provide_product_ingredients_repo)})
    async def delete_product_ingredient(
        self,
        product_ingredient_id: UUID,
        product_ingredients_repo: ProductIngredientRepository,
    ) -> None:
        """Create a new product ingredient."""
        await product_ingredients_repo.delete(product_ingredient_id)
        product_ingredients_repo.session.commit()


    @post(path="/{product_id:uuid}/product-size", dependencies={"product_size_repo": Provide(provide_product_size_repo)})
    async def create_product_size(
        self,
        product_id: UUID,
        product_size_repo: ProductSizeRepository,
        data: ProductSizeCreate,
    ) -> ProductSizeRead:
        """Create a new product ingredient."""
        obj = await product_size_repo.add(
            ProductSize(product_id=product_id,**data.model_dump(exclude_unset=True, exclude_none=True)),

        )
        await product_size_repo.session.commit()
        return ProductSizeRead.model_validate(obj)
    
    @delete(path="/{product_id:uuid}/product-size/{product_size_id:uuid}", dependencies={"product_size_repo": Provide(provide_product_size_repo)})
    async def delete_product_size(
        self,
        product_size_id: UUID,
        product_size_repo: ProductSizeRepository,
    ) -> None:
        """Create a new product size."""
        await product_size_repo.delete(product_size_id)
        product_size_repo.session.commit()


@get(path="/uploads/{filename:str}", exclude_from_auth=True)
async def serve_product_file(filename: str) -> Response:
    
    file_path = UPLOAD_DIRECTORY / filename
    if file_path.exists():
        return Response(
            content=file_path.read_bytes(),
            media_type="image/jpeg",
        )
    return Response(status_code=404)