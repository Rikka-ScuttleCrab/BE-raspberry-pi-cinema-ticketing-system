from pydantic import BaseModel
from datetime import date, datetime
from typing import List

class TicketDetailResponse(BaseModel):
    id: int
    movie_title: str
    show_date: date
    start_time: str
    theater_room_name: str
    seat_name: str
    created_at: datetime

    class Config:
        from_attributes = True