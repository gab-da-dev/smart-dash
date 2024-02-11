from typing import TYPE_CHECKING, ClassVar
from uuid import UUID

from litestar import Controller, delete, get, post, put

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