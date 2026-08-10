from sqlalchemy import Column, Integer, String, TIMESTAMP, text
from services.product_service.database import Base
from sqlalchemy.orm import relationship

class Category(Base):

    __tablename__ = "categories"

    category_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    category_name = Column(
        String(100),
        unique=True,
        nullable=False
    )

    created_at = Column(
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP")
    )

    # products = relationship(
    #     "Product",
    #     back_populates="category",
    #     cascade="all, delete"
    # )