from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    TIMESTAMP,
    Boolean
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from services.user_service.database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String(100), nullable=False)

    email = Column(String(255), unique=True, nullable=False)

    password = Column(String(255), nullable=False)

    phone = Column(String(15), unique=True, nullable=False)
    email_verified = Column(Boolean,default=False,nullable=False)

    phone_verified = Column(Boolean,default=False,nullable=False)

    role_id = Column(Integer, ForeignKey("roles.role_id"), nullable=False)

    created_at = Column(TIMESTAMP, server_default=func.now())

    role = relationship("Role", back_populates="users")

    addresses = relationship(
        "Address",
        back_populates="user",
        cascade="all, delete"
    )