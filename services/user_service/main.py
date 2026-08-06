from fastapi import FastAPI

from services.user_service.database import Base, engine

# Import models
from services.user_service.models import Role, User, Address

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="User Service",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "service": "User Service",
        "status": "Running"
    }