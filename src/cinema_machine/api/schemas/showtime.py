from pydantic import BaseModel
from typing import List, Optional
from api.schemas.type import TicketTypeSchema

class ReservedSeatsResponse(BaseModel):
    id: int
    seat_row: str
    seat_number: int

    class Config:
        from_attributes = True

class ShowtimeTodayResponse(BaseModel):
    id: int
    start_time: str
    ticket_type: Optional[TicketTypeSchema] = None
    theater_room_id: int
    theater_room_name: str
    reserved_seats: List[ReservedSeatsResponse]

    class Config:
        from_attributes = True