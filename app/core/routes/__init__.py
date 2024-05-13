from fastapi import APIRouter

from .user import user_router
from .auth import auth_router

core_router = APIRouter()

core_router.include_router(auth_router, tags=["Auth"])
core_router.include_router(user_router, tags=["User"])
