from fastapi import APIRouter
from app.api.endpoints import quotes

api_router = APIRouter()

api_router.include_router(quotes.router)
