from fastapi import FastAPI
from services.user_service.routers.user_router import router as user_router
from services.user_service.routers.auth_router import router as auth_router
from services.user_service.routers.admin_router import router as admin_router
from shared.config.settings import get_settings

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

# Add this
app.include_router(
    admin_router,
    prefix=settings.API_PREFIX
)

@app.get("/")
def root():
    return {
        "message": "User Service Running Successfully"
    }