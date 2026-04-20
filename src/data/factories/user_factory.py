from faker import Faker
from sqlalchemy.ext.asyncio import AsyncSession

from data.models.user_model import UserModel
from data.repositories import user_repository

fake = Faker()


async def create_user(
    db: AsyncSession,
    username: str | None = None,
    full_name: str | None = None,
    password: str | None = None,
) -> UserModel:
    return await user_repository.save(
        db,
        username=fake.pystr(3, 8) if username is None else username,
        full_name=fake.name() if full_name is None else full_name,
        hashed_password=fake.pystr(8) if password is None else password,
    )
