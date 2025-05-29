from fastapi import Depends
from sqlmodel import create_engine
from sqlalchemy import Engine
from typing import Annotated
from sqlmodel import Session, SQLModel

SQLITE_FILE_NAME = "app/db/data.db"

DATABASE_URL = f"sqlite:///{SQLITE_FILE_NAME}"

connect_args = {"check_same_thread": False}

engine: Engine = create_engine(DATABASE_URL, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
