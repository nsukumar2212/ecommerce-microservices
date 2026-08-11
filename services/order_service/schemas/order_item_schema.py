from pydantic import BaseModel, ConfigDict
from decimal import Decimal


class OrderItemResponse(BaseModel):
    order_item_id: int
    order_id: int
    product_id: int
    quantity: int
    price: Decimal

    model_config = ConfigDict(
        from_attributes=True
    )