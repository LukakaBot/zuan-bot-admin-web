from fastapi import APIRouter
from app.router.api import quote

api_router = APIRouter()

api_router.include_router(quote.router)
