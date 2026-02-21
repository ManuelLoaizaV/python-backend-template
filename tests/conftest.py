import pytest
from typing import Generator
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

from src.api.dependencies.db import get_db
from src.application.app import app
from src.infrastructure.database import Base, _sqlite_connect_args
from src.infrastructure.config import settings


@pytest.fixture
def client() -> Generator[TestClient, None, None]:
    engine_kwargs = {}
    if settings.test_database_url.startswith("sqlite"):
        engine_kwargs["poolclass"] = StaticPool

    engine = create_engine(
        settings.test_database_url,
        connect_args=_sqlite_connect_args(settings.test_database_url),
        **engine_kwargs,
    )
    testing_session_local = sessionmaker(bind=engine, autoflush=False, autocommit=False)

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    def override_get_db() -> Generator[Session, None, None]:
        db = testing_session_local()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()
    Base.metadata.drop_all(bind=engine)
