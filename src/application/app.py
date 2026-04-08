from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.dependencies.error_handlers import domain_exception_handler
from api.router import router as v1_router
from domain.exceptions.base import BaseDomainError
from infrastructure.config import settings
from infrastructure.postgres import engine


def create_app() -> FastAPI:
    app = FastAPI(title=settings.APP_NAME, lifespan=lifespan)
    app.add_exception_handler(BaseDomainError, domain_exception_handler)
    app.include_router(router=v1_router, prefix="/api/v1")
    return app


@asynccontextmanager
async def lifespan(_: FastAPI):
    from data.models.base import Base

    Base.metadata.create_all(engine)
    yield
