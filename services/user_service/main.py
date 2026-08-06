from fastapi import FastAPI

from services.user_service.routers.auth_router import router as auth_router

app = FastAPI(title="User Service")

app.include_router(auth_router)


@app.get("/")
def home():
    return {"message": "User Service Running"}