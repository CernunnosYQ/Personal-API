from fastapi import APIRouter

from .blogpost import blogpost_router

blog_router = APIRouter()

blog_router.include_router(blogpost_router)
