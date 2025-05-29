from fastapi import APIRouter
from app.api.endpoints import quote

api_router = APIRouter()

api_router.include_router(quote.router)
