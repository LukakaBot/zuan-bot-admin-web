from fastapi import FastAPI
from fastapi.routing import APIRoute
from app.api.main import api_router
from app.core.config import settings
from app.core.database import create_db_and_tables
import os


title = os.environ.get("SERVICE_PROJECT_NAME", "FastAPI") or settings.SERVICE_PROJECT_NAME
prefix = os.environ.get("SERVICE_API_PREFIX", "/api") or settings.SERVICE_API_PREFIX
host = os.environ.get("SERVICE_HOST", "0.0.0.0") or settings.SERVICE_HOST
port = int(os.environ.get("SERVICE_PORT", 8000)) or settings.SERVICE_PORT


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


app.include_router(api_router, prefix=prefix)

if __name__ == "__main__":
    uvicorn.run("app:main.app", host=host, port=port, reload=True)
