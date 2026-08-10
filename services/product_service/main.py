from fastapi import FastAPI
from services.product_service.routers.product_router import router as product_router
from shared.config.settings import get_settings
from services.product_service.routers.category_router import router as category_router

settings = get_settings()

app = FastAPI(
    title="Product Service",
    version="1.0.0"
)

app.include_router(
    category_router,
    prefix=settings.API_PREFIX
)
app.include_router(
    category_router,
    prefix=settings.API_PREFIX
)

app.include_router(
    product_router,
    prefix=settings.API_PREFIX
)

@app.get("/")
def root():
    return {
        "message": "Product Service Running Successfully"
    }