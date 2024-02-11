from typing import TYPE_CHECKING, ClassVar
from uuid import UUID

from litestar import Controller, delete, get, post, put
from sqlalchemy import desc, select

from schemas.product_schema import ProductCreate, ProductRead
# from ..db.models import models
from db.models import models
if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession


class ProductCommandController(Controller):
    path = "/product"
    # dependencies: ClassVar[dict[str, Provide]] = {"service": Provide(get_company_service)}
    tags: ClassVar[list[str]] = ["product_command"]

    @post()
    async def add(self, data: ProductCreate, db_session: "AsyncSession", db_engine: "AsyncEngine") -> ProductRead:
        product = models.Product(title=data.title,active=data.active,description=data.description,image=data.image,product_category_id=data.product_category_id,price=data.price,prep_time=data.prep_time,)
        print(product.to_dict())
        db_session.add(product)
        await db_session.commit()
        await db_session.refresh(product)
        return product.to_dict()
    

class ProductQueryController(Controller):
    path = "/product"
    # dependencies: ClassVar[dict[str, Provide]] = {"service": Provide(get_company_service)}
    tags: ClassVar[list[str]] = ["product_query"]

    @get("/{id_:uuid}")
    async def get_product(self, id_: UUID, db_session: "AsyncSession", db_engine: "AsyncEngine") -> list[ProductRead]:
        """Get a product by ID."""
        return list(await db_session.scalars(select(models.Product)))
        # load_options = (Order.load_files(), Order.load_schedules(), Order.load_group(), Order.load_requirements())
        # order = await repository.get(id_, load_options=load_options)
        return OrderReadDetail.from_orm(order)

    @get("/all")
    async def list_all_products(
        self,
         db_session: "AsyncSession", db_engine: "AsyncEngine")-> list[dict]:
        """Get a paginated list of products."""
        # load_options = Order.load_group()
        products = await db_session.scalars(select(models.Product))
        return [product.to_dict() for product in products] 