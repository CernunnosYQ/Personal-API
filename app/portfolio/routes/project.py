from fastapi import APIRouter

project_router = APIRouter()


@project_router.get("/read/project/all")
def _get_all_projects(db=None):
    """
    Show all projects
    """
    return {"message": "All projects"}


@project_router.get("/read/project/{id}")
def _get_project(db=None):
    return {"gessage": "Single project"}


@project_router.post("/create/project")
def _create_project(new_data, db=None):
    return {"message": "Create project"}


@project_router.put("/update/project/{id}")
def _update_project(id: int, db=None):
    return {"message": "Update project"}


@project_router.delete("/delete/project/{id}")
def _delete_project(id: int, db=None):
    return {"message": "Delete project"}
