from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from api.deps import get_db
from api.response import success_response, error_response
from services.ticketService import get_tickets_by_order_service
from api.schemas.ticket import TicketDetailResponse

router = APIRouter(prefix="/api/v1/tickets", tags=["Tickets"])

@router.get("/{booking_id}", response_model=List[TicketDetailResponse])
def get_tickets_by_booking(booking_id: int, db: Session = Depends(get_db)):

    tickets = get_tickets_by_order_service(db, booking_id)
    
    if not tickets:
        return error_response(
            error_detail="Không tìm thấy vé cho mã đặt này",
            status_code=404
        )

    return success_response(
        data=tickets,
        message="Lấy danh sách vé thành công"
    )