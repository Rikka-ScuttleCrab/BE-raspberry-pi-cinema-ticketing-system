from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.deps import get_db
from services.recommendationService import (
    recommend_movies_service
)

router = APIRouter(
    prefix="/api/v1/recommendations",
    tags=["Recommendations"]
)

@router.get("/{movie_id}")
def recommend_movies(
    movie_id: int,
    db: Session = Depends(get_db)
):
    return recommend_movies_service(
        db,
        movie_id
    )