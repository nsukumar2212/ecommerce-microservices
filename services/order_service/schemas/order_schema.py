from pydantic import BaseModel, ConfigDict
from decimal import Decimal
from datetime import datetime

from services.order_service.schemas.order_item_schema import OrderItemResponse


class OrderCreate(BaseModel):
    pass


class OrderResponse(BaseModel):
    order_id: int
    user_id: int
    total_amount: Decimal
    status: str
    created_at: datetime
    order_items: list[OrderItemResponse] = []

    model_config = ConfigDict(
        from_attributes=True
    )