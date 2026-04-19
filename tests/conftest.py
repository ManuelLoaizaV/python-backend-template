from collections.abc import AsyncGenerator

import pytest
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from infrastructure.postgres import get_session
from main import app

TEST_DATABASE_URL = "postgresql+psycopg://test_user:test_password@postgres-test:5432/test_db"
test_engine = create_async_engine(url=TEST_DATABASE_URL)
async_session = async_sessionmaker(bind=test_engine)


@pytest.fixture(autouse=True)
async def setup_database() -> AsyncGenerator[None]:
    from data.models.base import Base

    async with test_engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)

    yield

    async with test_engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)


@pytest.fixture
async def db_session() -> AsyncGenerator[AsyncSession]:
    async with async_session() as session, session.begin():
        yield session


@pytest.fixture
async def client(db_session: AsyncSession) -> AsyncGenerator[AsyncClient]:
    async def override_get_session() -> AsyncGenerator[AsyncSession]:
        yield db_session

    app.dependency_overrides[get_session] = override_get_session

    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://testserver",
    ) as test_client:
        yield test_client
    app.dependency_overrides.clear()
