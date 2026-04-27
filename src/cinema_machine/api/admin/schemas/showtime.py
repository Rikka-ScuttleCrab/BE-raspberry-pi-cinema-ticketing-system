from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class ShowtimeCreate(BaseModel):
    movie_id: int
    theater_room_id: int
    time_slot_id: int
    ticket_type_id: int
    dayshow: date


class ShowtimeUpdate(BaseModel):
    movie_id: Optional[int] = None
    theater_room_id: Optional[int] = None
    time_slot_id: Optional[int] = None
    ticket_type_id: Optional[int] = None
    dayshow: Optional[date] = None


class ShowtimeResponse(BaseModel):
    id: int
    movie_id: int
    movie_title: str
    theater_room_id: int
    dayshow: date
    start_time: str
    ticket_type: str

    class Config:
        from_attributes = True