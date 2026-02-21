from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from src.api.dependencies.db import get_db
from src.api.schemas.user_schemas import UserCreate, UserRead
from src.data.repositories.user_repository import UserRepository
from src.domain.services.user_service import UserService

router = APIRouter()


@router.get("", response_model=list[UserRead])
def list_users(
    db: Session = Depends(get_db),
    limit: int = Query(default=50, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    name: str | None = Query(default=None, min_length=1, max_length=100),
) -> list[UserRead]:
    service = UserService(UserRepository(db))
    users = service.list_users(limit=limit, offset=offset, name=name)
    return [UserRead(id=user.id, name=user.name) for user in users]


@router.post("", response_model=UserRead, status_code=201)
def create_user(payload: UserCreate, db: Session = Depends(get_db)) -> UserRead:
    service = UserService(UserRepository(db))
    user = service.create_user(name=payload.name)
    return UserRead(id=user.id, name=user.name)
