from fastapi import APIRouter

user_router = APIRouter()


@user_router.get("/read/user/{username}")
def _read_user(username, db=None):
    return {"user": "CernunnosYQ"}


@user_router.put("/update/user/{username}")
def _update_user_info(username, db=None):
    return {"message": f"Update {username}'s info"}


@user_router.delete("/delete/user/{username}")
def _delete_user(username, db=None):
    return {"message": "Delete user"}
