from sqlalchemy import select
from sqlalchemy.orm import Session

from data.models.user_model import UserModel


def get_by_username(db: Session, username: str) -> UserModel | None:
    statement = select(UserModel).where(UserModel.username == username)
    return db.execute(statement).scalar_one_or_none()


def save(db: Session, username: str, full_name: str, hashed_password: str) -> UserModel:
    user = UserModel(username=username, full_name=full_name, hashed_password=hashed_password)
    db.add(user)
    db.flush()
    db.refresh(user)
    return user
