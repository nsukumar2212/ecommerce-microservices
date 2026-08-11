from fastapi import FastAPI

from shared.config.settings import get_settings

from services.order_service.routers.order_router import (
    router as order_router
)


settings = get_settings()


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)


app.include_router(
    order_router,
    prefix=settings.API_PREFIX
)


@app.get("/")
def root():
    return {
        "message": "Order Service Running Successfully"
    }