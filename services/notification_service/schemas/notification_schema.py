from datetime import datetime

from pydantic import BaseModel, ConfigDict


class NotificationCreate(BaseModel):
    user_id: int
    order_id: int | None = None
    type: str
    message: str


class NotificationResponse(BaseModel):
    notification_id: int
    user_id: int
    order_id: int | None
    type: str
    message: str
    status: str
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )