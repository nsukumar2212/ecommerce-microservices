from decimal import Decimal
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class PaymentCreate(BaseModel):
    order_id: int
    amount: Decimal
    payment_method: str


class PaymentResponse(BaseModel):
    payment_id: int
    order_id: int
    user_id: int
    amount: Decimal
    payment_method: str
    transaction_id: str | None = None
    status: str
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )