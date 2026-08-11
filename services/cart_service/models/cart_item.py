from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from services.cart_service.database import Base


class CartItem(Base):

    __tablename__ = "cart_items"

    cart_item_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    cart_id = Column(
        Integer,
        ForeignKey("cart.cart_id", ondelete="CASCADE"),
        nullable=False
    )

    product_id = Column(
        Integer,
        nullable=False
    )

    quantity = Column(
        Integer,
        nullable=False,
        default=1
    )

    cart = relationship(
        "Cart",
        back_populates="cart_items"
    )