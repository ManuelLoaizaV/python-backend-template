from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.api.dependencies.db import get_db
from src.api.schemas.user_schemas import UserCreate, UserRead
from src.data.repositories.user_repository import UserRepository
from src.domain.services.user_service import UserService

router = APIRouter()


@router.get("", response_model=list[UserRead])
def list_users(db: Session = Depends(get_db)) -> list[UserRead]:
    service = UserService(UserRepository(db))
    users = service.list_users()
    return [UserRead(id=user.id, name=user.name) for user in users]


@router.post("", response_model=UserRead, status_code=201)
def create_user(payload: UserCreate, db: Session = Depends(get_db)) -> UserRead:
    service = UserService(UserRepository(db))
    user = service.create_user(name=payload.name)
    return UserRead(id=user.id, name=user.name)
