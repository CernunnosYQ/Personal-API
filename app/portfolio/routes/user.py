from fastapi import APIRouter

user_router = APIRouter()

@user_router.get("/get/user")
def _get_user(db=None):
    """
    Get the default user with the portfolio data
    """
    return {"message": "This is the user"}


@user_router.put("/update/user")
def _update_user(user, db=None):
    """
    Update the user's portfolio data
    """
    return {"message": "User data updated"}