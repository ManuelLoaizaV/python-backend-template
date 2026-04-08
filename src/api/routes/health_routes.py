from fastapi import APIRouter, Response, status

health_router = APIRouter()


@health_router.get(
    path="/",
    status_code=status.HTTP_204_NO_CONTENT,
    response_class=Response,
)
async def health_check() -> None:
    """Check the operational health of the application."""
