from fastapi import FastAPI

from shared.config.settings import get_settings

from services.cart_service.routers.cart_router import router as cart_router
from services.cart_service.routers.cart_item_router import router as cart_item_router


settings = get_settings()


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)


app.include_router(
    cart_router,
    prefix=settings.API_PREFIX
)

app.include_router(
    cart_item_router,
    prefix=settings.API_PREFIX
)


@app.get("/")
def root():
    return {
        "message": "Cart Service Running Successfully"
    }