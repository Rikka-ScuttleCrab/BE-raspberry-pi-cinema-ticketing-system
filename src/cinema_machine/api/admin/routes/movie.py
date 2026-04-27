import math
from core.security.role import has_role
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from api.response import success_response, error_response
from api.deps import get_db, get_current_user_token
from api.admin.schemas.movie import (
    MovieAdminResponse,
    MovieCreateAdmin,
    MovieUpdateAdmin
)

from api.admin.services.movieService import (
    get_all_movies_service,
    create_movie_admin_service,
    update_movie_admin_service
)

router = APIRouter(prefix="/movies", tags=["Movies"])

@router.get("/")
def get_all_movies(
    page: int = Query(1, ge=1),
    db: Session = Depends(get_db),
    token_data: dict = Depends(get_current_user_token)
):
    if not has_role(token_data, "admin"):
        return error_response("Permission denied", status_code=403)

    raw = get_all_movies_service(db, page=page)

    items = [
        MovieAdminResponse.model_validate(m).model_dump(mode="json")
        for m in raw["items"]
    ]

    page_size = 30
    total = raw["total"]
    total_pages = math.ceil(total / page_size)

    return success_response(
        data={
            "page": page,
            "page_size": page_size,
            "total": total,
            "total_pages": total_pages,
            "items": items,
        },
        message="GET ALL MOVIES SUCCESS"
    )
    
@router.post("/")
def create_movie(
    payload: MovieCreateAdmin,
    db: Session = Depends(get_db),
    token_data: dict = Depends(get_current_user_token)
):
    if not has_role(token_data, "admin"):
        return error_response("Permission denied", status_code=403)

    try:
        movie = create_movie_admin_service(db, payload)

        return success_response(
            data={"id": movie.id},
            message="CREATE MOVIE SUCCESS",
            status_code=201
        )

    except ValueError as e:
        return error_response(str(e), status_code=400)


@router.put("/{movie_id}")
def update_movie(
    movie_id: int,
    payload: MovieUpdateAdmin,
    db: Session = Depends(get_db),
    token_data: dict = Depends(get_current_user_token)
):
    if not has_role(token_data, "admin"):
        return error_response("Permission denied", status_code=403)

    try:
        movie = update_movie_admin_service(db, movie_id, payload)

        if not movie:
            return error_response("Movie not found", status_code=404)

        return success_response(
            data={"id": movie.id},
            message="UPDATE MOVIE SUCCESS"
        )

    except ValueError as e:
        return error_response(str(e), status_code=400)