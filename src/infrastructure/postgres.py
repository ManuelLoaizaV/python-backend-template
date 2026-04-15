from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from infrastructure.config import settings

engine = create_async_engine(url=str(settings.SQLALCHEMY_DATABASE_URI))
async_session = async_sessionmaker(bind=engine)


async def get_session() -> AsyncGenerator[AsyncSession]:
    async with async_session() as session, session.begin():
        yield session
