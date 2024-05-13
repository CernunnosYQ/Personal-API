from fastapi import FastAPI

from core.config import settings

from app.portfolio import portfolio_router
from app.blog import blog_router
from app.core import core_router


def includeRouters(app: FastAPI):
    app.include_router(core_router, prefix="/api")
    app.include_router(portfolio_router, prefix="/api/portfolio", tags=["Portfolio"])
    app.include_router(blog_router, prefix="/api/portfolio", tags=["Blog"])


def createApp() -> FastAPI:
    app = FastAPI()
    includeRouters(app)
    return app


app = createApp()


@app.get("/")
async def root():
    return {"message": f"Welcome to {settings.PROJECT_NAME} {settings.VERSION}"}
