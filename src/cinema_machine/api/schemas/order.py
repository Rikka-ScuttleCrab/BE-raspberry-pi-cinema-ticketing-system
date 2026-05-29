from pydantic import BaseModel
from typing import List, Optional
from  api.schemas.seat import SeatSelection
from datetime import datetime

class OrderRequest(BaseModel):
    showtime_id: int
    voucher_id: Optional[int] = None
    guest_name: str
    info: str
    seats: List[SeatSelection]
    
class OrderResponse(BaseModel):
    order_id: int
    guest_name: str
    total_amount: int
    voucher_code: str
    payment_order_code: int
    paid_at: datetime