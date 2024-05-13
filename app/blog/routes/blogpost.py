from fastapi import APIRouter

blogpost_router = APIRouter()


@blogpost_router.get("/read/blogpost/all")
def _get_all_blogpost(db=None):
    """
    Get a blogpost by his slug
    """
    return {"message": "This are all blogposts"}


@blogpost_router.get("/read/blogpost/{slug}")
def _get_blogpost(slug: str, db=None):
    """
    Get a blogpost by his slug
    """
    return {"message": f"This is {slug} blogpost"}


@blogpost_router.post("/create/blogpost/")
def _create_blogpost(new_post, db=None):
    """
    Create new blogpost and returns it
    """
    return {"message": "Blogpost created"}


@blogpost_router.put("/update/blogpost/{id}")
def _update_blogpost(id: int, new_data, db=None):
    """
    Updates an existing blogpost by his id
    """
    return {"message": "Blogpost updated"}


@blogpost_router.delete("/delete/blogpost/{id}")
def _delete_blogpost(id: int, db=None):
    """
    Delete a blogpost by its id
    """
    return {"message": "Blogpost deleted"}
