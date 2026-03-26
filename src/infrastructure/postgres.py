from sqlalchemy import create_engine

from infrastructure.config import settings

engine = create_engine(url=str(settings.postgres_database_url))
