from fastapi import APIRouter
from sqlmodel import SQLModel, Field
from sqlalchemy import func
from fastapi.responses import JSONResponse
from app.core.database import SessionDep

router = APIRouter(tags=["quote"])


class Main(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    text: str


@router.get("/")
def getQuote(db: SessionDep):
    quote: Main = db.query(Main).order_by(func.random()).first()

    if not quote:
        return JSONResponse(
            content={
                "code": 400,
                "message": "No quotes found!",
                "data": None,
            }
        )

    return JSONResponse(content={"code": 200, "message": "Success", "data": quote.text})
