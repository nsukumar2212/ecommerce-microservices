from fastapi import FastAPI

from shared.config.settings import get_settings

from services.payment_service.routers.payment_router import (
    router as payment_router
)


settings = get_settings()


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)


app.include_router(
    payment_router,
    prefix=settings.API_PREFIX
)


@app.get("/")
def root():
    return {
        "message": "Payment Service Running Successfully"
    }