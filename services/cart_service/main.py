from fastapi import FastAPI

from shared.config.settings import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)


@app.get("/")
def root():
    return {
        "message": "Cart Service Running Successfully"
    }