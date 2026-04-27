from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from api.response import success_response, error_response
from api.deps import get_db, get_current_user_token
from api.schemas.movie import MovieBase, MovieDetailResponse
from core.security.role import has_role


from services.movieService import (
    get_movie_by_id_service,
    get_showing_movies_service,
    get_all_movies_service
)

router = APIRouter(prefix="/api/v1/movies", tags=["Movies"])

@router.get("/now-showing")
def get_now_showing_movies(db: Session = Depends(get_db)):

    movies = get_showing_movies_service(db)

    data = [
        MovieBase.model_validate(m).model_dump(mode="json")
        for m in movies
    ]

    return success_response(
        data=data,
        message="GET NOW SHOWING MOVIES SUCCESS"
    )

@router.get("/{movie_id}")
def get_movie(movie_id: int, db: Session = Depends(get_db)):

    raw = get_movie_by_id_service(db, movie_id)

    if not raw:
        return error_response("Movie not found", status_code=404)

    data = MovieDetailResponse.model_validate(raw).model_dump(mode="json")

    return success_response(data=data)

@router.get("/")
def get_all_movies(
    page: int = Query(1, ge=1),
    db: Session = Depends(get_db),
    token_data: dict = Depends(get_current_user_token)
):
    # 🔐 check admin
    if not has_role(token_data, "admin"):
        return error_response("Permission denied", status_code=403)

    data = get_all_movies_service(db, page=page)

    return success_response(
        data=data,
        message="GET ALL MOVIES SUCCESS"
    )
