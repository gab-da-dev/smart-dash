from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, ClassVar
from uuid import UUID
from advanced_alchemy import NotFoundError

from pydantic import BaseModel as _BaseModel, TypeAdapter
# from pydantic import TypeAdapter

from litestar import Litestar, get, put
from litestar.controller import Controller
from litestar.di import Provide
from litestar.handlers.http_handlers.decorators import delete, post
from litestar.pagination import OffsetPagination
from litestar.params import Parameter
from litestar.repository.filters import LimitOffset
from schemas.order_schema import OrderCreate, OrderProductCreate, OrderRead, OrderUpdate
from db.models.models import Order, OrderProduct

from db.repositories.order_repository import OrderRepository, provide_order_details_repo, provide_order_repo
from db.repositories.order_product_repository import OrderProductRepository, provide_order_product_details_repo, provide_order_product_repo
if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession



class OrderController(Controller):
    path = "/order"
    dependencies:ClassVar[dict[str, Provide]] = {"repository": Provide(provide_order_repo)}

    tags: ClassVar[list[str]] = ["order"]

    @post(path="/", dependencies={"order_product_repo": Provide(provide_order_product_repo)})
    async def create_order(
        self,
        repository: OrderRepository,
        order_product_repo: OrderProductRepository,
        data: OrderCreate,
    ) -> OrderRead:
        """Create a new Order."""
        obj = await repository.add(
            Order(**data.model_dump(exclude_unset=True, exclude_none=True, exclude=['order'])),

        )
        await repository.session.commit()

        order_product = data.order
        order_array = []
        
        for order in order_product:
            order_product_obj = order.model_dump()
            order_product_obj['order_id'] = obj.id
            order_array.append(order_product_obj)
            await order_product_repo.add(OrderProduct(order_id=order_product_obj['order_id'],note=order_product_obj['note'],product_id=order_product_obj['product_id'],quantity=order_product_obj['quantity'],price=order_product_obj['price']))
        
        await order_product_repo.session.commit()
        
        return OrderRead.model_validate(obj)

       
    @get(path="/{order_id:uuid}", dependencies={"orders_repo": Provide(provide_order_details_repo)})
    async def get_order(
        self,
        orders_repo: OrderRepository,
        order_id: UUID = Parameter(
            title="order ID",
            description="The order to retrieve.",
        ),
    ) -> OrderRead:
        """Get an existing order."""
        
        obj = await orders_repo.get(order_id)
        # obj = await orders_repo.get_one_or_none(product_id)
        return OrderRead.model_validate(obj)
        
    # TODO: check how to put in a not found exception
    
    @get("/all")
    async def list_all_order(
        self,
        repository: OrderRepository,
        limit_offset: LimitOffset,
        )-> OffsetPagination[Order]:
        """Get list of orders."""
        results, total = await repository.list_and_count(limit_offset)
        type_adapter = TypeAdapter(list[OrderRead])
        return OffsetPagination[OrderRead](
            items=type_adapter.validate_python(results),
            total=total,
            limit=limit_offset.limit,
            offset=limit_offset.offset,
        )
    
    @put(path="/{order_id:uuid}")
    async def update_order(
        self,
        repository: OrderRepository,
        data: OrderUpdate,
        order_id: UUID = Parameter(
            title="Order ID",
            description="The order to update.",
        ),
    ) -> OrderRead:
        """Update an order."""

        raw_obj = data.model_dump(exclude_unset=True, exclude_none=True)
        raw_obj.update({"id": order_id})
        obj = await repository.update(Order(**raw_obj))
        await repository.session.commit()
        return OrderRead.from_orm(obj)


    @delete(path="/{order_id:uuid}")
    async def delete_order(
        self,
        repository: OrderRepository,
        order_id: UUID = Parameter(
            title="order ID",
            description="The order to delete.",
        ),
    ) -> None:
        """Delete a order from the system."""

        _ = await repository.delete(order_id)
        await repository.session.commit()


