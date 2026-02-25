from fastapi import APIRouter

from api.routes import health_routes, user_routes

api_router = APIRouter()
api_router.include_router(health_routes.router, tags=["health"])
api_router.include_router(user_routes.router, prefix="/users", tags=["users"])
