from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from api.response import success_response, error_response
from api.deps import get_db
from api.schemas.showtime import ShowtimeTodayResponse
from services.showtimeService import get_today_showtimes_with_reserved_seats

router = APIRouter(prefix="/api/v1/showtimes", tags=["Showtimes"])

@router.get("/today/{movie_id}")
def get_today_showtimes(movie_id: int, db: Session = Depends(get_db)):
    """
    Lấy danh sách suất chiếu trong ngày của một phim cụ thể, 
    bao gồm thông tin phòng và các ghế đã được đặt.
    """
    showtimes = get_today_showtimes_with_reserved_seats(db, movie_id)
    if not showtimes:
        return success_response(
            data=[], 
            message="NO SHOWTIMES AVAILABLE FOR THIS MOVIE TODAY"
        )
    data = [
        ShowtimeTodayResponse.model_validate(s).model_dump(mode="json")
        for s in showtimes
    ]
    return success_response(
        data=data,
        message="GET TODAY SHOWTIMES SUCCESS"
    )