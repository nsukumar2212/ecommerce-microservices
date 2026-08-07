from fastapi import FastAPI
from services.user_service.routers.user_router import router as user_router
from shared.config.settings import get_settings
from services.user_service.routers.auth_router import router as auth_router

settings = get_settings()

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

app.include_router(
    auth_router,
    prefix=settings.API_PREFIX
)
app.include_router(
    user_router,
    prefix=settings.API_PREFIX
)


@app.get("/")
def root():
    return {
        "message": "User Service Running Successfully"
    }