from fastapi import APIRouter

auth_router = APIRouter()


@auth_router.post("/login")
def _login_for_access_token(db=None):
    return {"message": "Login user"}


@auth_router.post("/register")
def _login_for_access_token(db=None):
    return {"message": "Login user"}


@auth_router.post("/update/password/{username}")
def _change_password(username, db=None):
    return {"message": f"Update password from {username}"}


@auth_router.post("/restore/password/{username}")
def _restore_password(username, db=None):
    return {"message": f"Restore Password"}
