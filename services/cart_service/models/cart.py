from sqlalchemy import Column, Integer, TIMESTAMP, text
from sqlalchemy.orm import relationship

from services.cart_service.database import Base


class Cart(Base):

    __tablename__ = "cart"

    cart_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        nullable=False
    )

    created_at = Column(
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP")
    )

    cart_items = relationship(
        "CartItem",
        back_populates="cart",
        cascade="all, delete"
    )