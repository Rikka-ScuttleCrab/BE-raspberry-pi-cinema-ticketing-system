from pydantic import BaseModel


class SeatSelection(BaseModel):
    seat_row: str
    seat_number: int