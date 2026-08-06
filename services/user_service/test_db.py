from sqlalchemy import text
from services.user_service.database import engine

with engine.connect() as connection:
    result = connection.execute(text("SELECT DATABASE()"))
    print("Connected Database:", result.scalar())