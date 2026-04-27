from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from api.deps import get_db, get_current_user_token
from api.response import success_response, error_response
from core.security.role import has_role

from api.admin.schemas.ticket import TicketResponse
from api.admin.services.ticketService import (
    get_all_tickets_service,
    cancel_ticket_service
)

router = APIRouter(prefix="/tickets", tags=["Tickets"])


@router.get("/")
def get_all_tickets(
    page: int = Query(1, ge=1),
    db: Session = Depends(get_db),
    token_data: dict = Depends(get_current_user_token)
):
    if not has_role(token_data, "admin"):
        return error_response("Permission denied", 403)

    raw = get_all_tickets_service(db, page=page)

    data = [
        TicketResponse.model_validate(i).model_dump(mode="json")
        for i in raw["items"]
    ]

    return success_response(
        data={
            "items": data,
            "page": page,
            "total": raw["total"],
            "total_pages": (raw["total"] + 29) // 30
        },
        message="GET ALL TICKETS SUCCESS"
    )
    
@router.put("/{ticket_id}/cancel")
def cancel_ticket(
    ticket_id: int,
    db: Session = Depends(get_db),
    token_data: dict = Depends(get_current_user_token)
):
    if not has_role(token_data, "admin"):
        return error_response("Permission denied", 403)

    try:
        ticket = cancel_ticket_service(db, ticket_id)

        if not ticket:
            return error_response("Ticket not found", 404)

        return success_response(
            data={"id": ticket.id, "status": ticket.status},
            message="CANCEL TICKET SUCCESS"
        )

    except ValueError as e:
        return error_response(str(e))