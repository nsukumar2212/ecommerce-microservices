from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from services.user_service.database import Base


class Address(Base):
    __tablename__ = "addresses"

    address_id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.user_id"))

    address_line = Column(String(255), nullable=False)

    city = Column(String(100), nullable=False)

    state = Column(String(100), nullable=False)

    pincode = Column(String(10), nullable=False)

    country = Column(String(100), nullable=False)

    created_at = Column(TIMESTAMP, server_default=func.now())

    user = relationship("User", back_populates="addresses")