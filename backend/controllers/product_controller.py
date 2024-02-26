from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING
from uuid import UUID

from pydantic import BaseModel as _BaseModel
from pydantic import TypeAdapter
from sqlalchemy import ForeignKey, select
from sqlalchemy.orm import Mapped, mapped_column, relationship, selectinload,joinedload

from litestar import Litestar, get
from litestar.contrib.sqlalchemy.base import UUIDAuditBase, UUIDBase
from litestar.contrib.sqlalchemy.plugins import AsyncSessionConfig, SQLAlchemyAsyncConfig, SQLAlchemyInitPlugin
from litestar.contrib.sqlalchemy.repository import SQLAlchemyAsyncRepository
from litestar.controller import Controller
from litestar.di import Provide
from litestar.handlers.http_handlers.decorators import delete, patch, post
from litestar.pagination import OffsetPagination
from litestar.params import Parameter
from litestar.repository.filters import LimitOffset
from schemas.product_schema import ProductRead
from db.models.models import Product

from db.repositories.product_repository import ProductRepository, provide_products_repo

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class ProductCommandController(Controller):
    path = "/product"
    # dependencies: ClassVar[dict[str, Provide]] = {"service": Provide(get_company_service)}
    # tags: ClassVar[list[str]] = ["product_command"]

    # @post()
    # async def add(self, data: ProductCreate, db_session: "AsyncSession", db_engine: "AsyncEngine") -> ProductRead:
    #     product = models.Product(title=data.title,active=data.active,description=data.description,image=data.image,product_category_id=data.product_category_id,price=data.price,prep_time=data.prep_time,)
    #     print(product.to_dict())
    #     db_session.add(product)
    #     await db_session.commit()
    #     await db_session.refresh(product)
    #     return ProductRead
    

class ProductQueryController(Controller):
    path = "/product"
    dependencies = {"products_repo": Provide(provide_products_repo, sync_to_thread=False)}

    tags: ClassVar[list[str]] = ["product_query"]

    # @get("/{id_:uuid}")
    # async def get_product(self, id_: UUID, db_session: "AsyncSession", db_engine: "AsyncEngine") -> list[ProductRead]:
    #     """Get a product by ID."""
    #     product = db_session.scalars(select())
    #     # return list(await db_session.scalars(select(models.Product)))
    #     # load_options = (Order.load_files(), Order.load_schedules(), Order.load_group(), Order.load_requirements())
    #     # order = await repository.get(id_, load_options=load_options)
    #     return OrderReadDetail.from_orm(order)



    @get(path="/list")
    async def list_products(
        self,
        products_repo: ProductRepository,
        limit_offset: LimitOffset,
    ) -> OffsetPagination[ProductRead]:
        """List products."""
        results, total = await products_repo.list_and_count(limit_offset)
        type_adapter = TypeAdapter(list[ProductRead])
        return OffsetPagination[ProductRead](
            items=type_adapter.validate_python(results),
            total=total,
            limit=limit_offset.limit,
            offset=limit_offset.offset,)
    
    # @get("/all")
    # async def list_all_products(
    #     self,
    #      db_session: "AsyncSessionConfig", db_engine: "AsyncEngine")-> list[ProductRead]:
    #     """Get list of products."""
    #     products = await db_session.scalars(select(models.Product))
    #     return [ProductRead.from_orm(product) for product in products]
        # products = await db_session.query(models.Product).options(
        # selectinload(models.Product.product_ingredients)
        # ).all()

        # # Convert to Pydantic models (casting not explicitly needed with 'orm_mode=True')
        # product_reads = [ProductRead.from_orm(product) for product in products]

        # return product_reads

        # query = select(models.Product).options(selectinload(models.Product.product_ingredients))
        # result = await db_session.execute(query)
        # products = result.scalars().all()
        # products_read = []
        # for product in products:
        #     product_ingredients_list = [
        #         {
        #             "name": ingredient.name,
        #             # Include other fields as needed (e.g., price, active)
        #         }
        #         for ingredient in product.product_ingredients
        #     ]
        #     product_read = ProductRead(
        #         id=product.id,
        #         name=product.name,
        #         description=product.description,
        #         image=product.image,
        #         product_category_id=product.product_category_id,
        #         price=product.price,
        #         prep_time=product.prep_time,
        #         active=product.active,
        #         # ...other fields
        #         product_ingredients=product_ingredients_list
        #     )
        #     products_read.append(product_read)

        # return products_read 