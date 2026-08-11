from fastapi import FastAPI

from shared.config.settings import get_settings

from services.notification_service.routers.notification_router import (
    router as notification_router
)


settings = get_settings()


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)


app.include_router(
    notification_router,
    prefix=settings.API_PREFIX
)


@app.get("/")
def root():
    return {
        "message": "Notification Service Running Successfully"
    }