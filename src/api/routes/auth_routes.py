from fastapi import APIRouter, status

from api.schemas.auth_schemas import RegisterRequest

auth_router = APIRouter()


@auth_router.post(
    path="/register",
    response_model=None,
    status_code=status.HTTP_201_CREATED,
)
async def register(register_request: RegisterRequest):
    return
