from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from api.deps import get_db
from api.response import success_response, error_response
from services.ticketService import get_tickets_by_order_service, send_tickets_service, verify_ticket_service
from api.schemas.ticket import TicketDetailResponse
from services.security_service import (
    generate_signature
)
router = APIRouter(prefix="/api/v1/tickets", tags=["Tickets"])

@router.get("/{order_id}", response_model=List[TicketDetailResponse])
def get_tickets_by_order(order_id: int, db: Session = Depends(get_db)):

    tickets = get_tickets_by_order_service(db, order_id)
    
    if not tickets:
        return error_response(
            error_detail="Không tìm thấy vé cho mã đặt này",
            status_code=404
        )

    return success_response(
        data=tickets,
        message="Lấy danh sách vé thành công"
    )
    
@router.post("/send/{order_id}")
async def send_ticket(
    order_id: int,
    db: Session = Depends(get_db)
):
    return await send_tickets_service(
        db,
        order_id
    )
    
@router.get("/verify/{order_id}")
async def verify_ticket(
    order_id: int,
    sig: str,
    db: Session = Depends(get_db)
):

    expected_sig = generate_signature(
        order_id
    )

    if sig != expected_sig:

        return {
            "success": False,
            "message": "Invalid QR signature"
        }
    return verify_ticket_service(
        db,
        order_id
    )