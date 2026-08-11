from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    TIMESTAMP,
    text
)

from services.notification_service.database import Base


class Notification(Base):

    __tablename__ = "notifications"

    notification_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        nullable=False
    )

    order_id = Column(
        Integer,
        nullable=True
    )

    type = Column(
        String(50),
        nullable=False
    )

    message = Column(
        Text,
        nullable=False
    )

    status = Column(
        String(50),
        nullable=False,
        default="unread"
    )

    created_at = Column(
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP")
    )