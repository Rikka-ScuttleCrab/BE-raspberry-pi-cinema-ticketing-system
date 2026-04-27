from pydantic import BaseModel
from typing import Optional
from datetime import date

class TicketResponse(BaseModel):
    id: int

    order_id: int
    guest_name: Optional[str]

    showtime_id: int
    movie_title: str
    dayshow: date
    start_time: str

    seat_row: str
    seat_number: int

    status: str
    
    class Config:
        from_attributes = True