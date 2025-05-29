from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(tags=["quotes"])


@router.get("/")
def getQuotes():
    return JSONResponse(content={"message": "Hello, Zuan!"})
