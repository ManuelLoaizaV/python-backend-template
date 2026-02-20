from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.api.router import api_router
from src.infrastructure.config import settings
from src.infrastructure.database import create_tables
from src.infrastructure.logging import configure_logging


@asynccontextmanager
async def lifespan(_: FastAPI):
    configure_logging()
    create_tables()
    yield


app = FastAPI(title=settings.app_name, lifespan=lifespan)
app.include_router(api_router)
