from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.router import router as v1_router
from infrastructure.config import settings
from infrastructure.postgres import engine


def create_app() -> FastAPI:
    app = FastAPI(title=settings.APP_NAME, lifespan=lifespan)
    app.include_router(router=v1_router, prefix="/api/v1")
    return app


@asynccontextmanager
async def lifespan(_: FastAPI):
    with engine.connect() as connection:
        from sqlalchemy import text

        result = connection.execute(statement=text("select 'hello world'"))
        print(result.all())
    yield
