from fastapi import APIRouter
from src.apps.utils.api import utils


api_router = APIRouter()

api_router.include_router(utils, prefix="/utils", tags=["utils"])
