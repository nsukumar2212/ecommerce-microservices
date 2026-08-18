from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DECIMAL,
    ForeignKey,
    TIMESTAMP,
    text
)

from sqlalchemy.orm import relationship

from services.product_service.database import Base
from services.product_service.models.category import Category

class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, index=True)

    product_name = Column(String(200), nullable=False)

    brand = Column(String(100), nullable=False)

    price = Column(DECIMAL(10, 2), nullable=False)

    description = Column(Text)

    image = Column(Text)
    stock = Column(Integer, nullable=False)

    category_id = Column(
        Integer,
        ForeignKey("categories.category_id")
    )

    created_at = Column(
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP")
    )

    category = relationship("Category")