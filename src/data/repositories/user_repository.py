from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from data.models.user_model import UserModel


async def get_by_username(db: AsyncSession, username: str) -> UserModel | None:
    statement = select(UserModel).where(UserModel.username == username)
    result = await db.execute(statement)
    return result.scalar_one_or_none()


async def save(db: AsyncSession, username: str, full_name: str, hashed_password: str) -> UserModel:
    user = UserModel(username=username, full_name=full_name, hashed_password=hashed_password)
    db.add(user)
    await db.flush()
    await db.refresh(user)
    return user
