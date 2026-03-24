from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.router import router as v1_router
from infrastructure.config import settings


def create_app() -> FastAPI:
    app = FastAPI(title=settings.app_name, lifespan=lifespan)
    app.include_router(router=v1_router, prefix="/api/v1")
    return app


@asynccontextmanager
async def lifespan(_: FastAPI):
    yield
