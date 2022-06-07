from fastapi import FastAPI

from src.config import settings
from src.apps import routers

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="0.0.2"
)


app.include_router(routers.api_router, prefix=settings.API_V1_STR)
