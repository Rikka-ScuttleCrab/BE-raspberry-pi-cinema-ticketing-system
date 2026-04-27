from pydantic import BaseModel
from typing import List, Optional
from  api.schemas.seat import SeatSelection


class OrderRequest(BaseModel):
    showtime_id: int
    voucher_id: Optional[int] = None
    guest_name: str
    info: str
    seats: List[SeatSelection]