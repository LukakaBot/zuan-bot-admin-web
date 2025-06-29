from fastapi import FastAPI
from fastapi.routing import APIRoute
from app.router.main import api_router
from app.core.database import create_db_and_tables
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

title = os.environ.get("SERVICE_PROJECT_NAME", "FastAPI")
prefix = os.environ.get("SERVICE_API_PREFIX", "/api")

origins = [
    "http://localhost",
    "http://localhost:3301",
    "http://192.168.1.191:3301",
    "https://zuan.lukaka.work/",
]


def generate_unique_id(route: APIRoute):
    return f"{route.tags[0]}-{route.name}"


app = FastAPI(
    title=title,
    openapi_url=f"{prefix}/openapi.json",
    generate_unique_id_function=generate_unique_id,
)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=prefix)
