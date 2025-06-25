from fastapi import APIRouter
from sqlmodel import SQLModel, Field, select
from sqlalchemy import func
from fastapi.responses import JSONResponse
from app.core.database import SessionDep

router = APIRouter(tags=["quote"])


class Main(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    text: str
    level: str


@router.get("/quote")
def getQuote(db: SessionDep, level: str = "min"):
    statement = select(Main).where(Main.level == level).order_by(func.random()).limit(1)
    quote: Main = db.exec(statement).first()

    if not quote:
        return JSONResponse(
            content={
                "code": 400,
                "message": "no quote found!",
                "data": None,
            }
        )

    return JSONResponse(content={"code": 200, "message": "success", "data": quote.text})
