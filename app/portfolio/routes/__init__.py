from fastapi import APIRouter

from .user import user_router
from .project import project_router

portfolio_router = APIRouter()
portfolio_router.include_router(user_router)
portfolio_router.include_router(project_router)
