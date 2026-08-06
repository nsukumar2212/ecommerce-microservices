from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from services.user_service.database import Base


class Role(Base):
    __tablename__ = "roles"

    role_id = Column(Integer, primary_key=True, index=True)

    role_name = Column(String(30), unique=True, nullable=False)

    created_at = Column(DateTime, server_default=func.now())