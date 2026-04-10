from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from infrastructure.config import settings

engine = create_engine(url=str(settings.SQLALCHEMY_DATABASE_URI))


def get_session() -> Generator[Session]:
    with Session(bind=engine) as session, session.begin():
        yield session
