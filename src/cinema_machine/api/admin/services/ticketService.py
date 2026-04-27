from datetime import datetime, timedelta

from sqlalchemy.orm import Session, joinedload


from models.tickets.ticket import Ticket
from models.tickets.order import Order
from models.theaters.showtime import Showtime


def get_all_tickets_service(db: Session, page: int = 1, page_size: int = 30):

    offset = (page - 1) * page_size

    total = db.query(Ticket).count()

    tickets = (
        db.query(Ticket)
        .options(
            joinedload(Ticket.order)
                .joinedload(Order.showtime)
                .joinedload(Showtime.movie),

            joinedload(Ticket.order)
                .joinedload(Order.showtime)
                .joinedload(Showtime.time_slot),

            joinedload(Ticket.seat)
        )
        .order_by(Ticket.id.desc())
        .offset(offset)
        .limit(page_size)
        .all()
    )

    items = []

    for t in tickets:
        showtime = t.order.showtime if t.order else None

        items.append({
            "id": t.id,
            "order_id": t.order_id,
            "guest_name": t.order.guest_name if t.order else None,

            "showtime_id": showtime.id if showtime else None,
            "movie_title": showtime.movie.title if showtime and showtime.movie else None,
            "dayshow": showtime.dayshow if showtime else None,
            "start_time": showtime.time_slot.start_time if showtime else None,

            "seat_row": t.seat.seat_row if t.seat else None,
            "seat_number": t.seat.seat_number if t.seat else None,
            
            "status": t.status,
        })

    return {
        "items": items,
        "total": total
    }
    
def cancel_ticket_service(db: Session, ticket_id: int):

    ticket = (
        db.query(Ticket)
        .options(
            joinedload(Ticket.order)
                .joinedload(Order.showtime)
                .joinedload(Showtime.time_slot),

            joinedload(Ticket.order)
                .joinedload(Order.showtime)
                .joinedload(Showtime.ticket_type),

            joinedload(Ticket.order)
                .joinedload(Order.tickets)
        )
        .filter(Ticket.id == ticket_id)
        .first()
    )

    if not ticket:
        return None

    if ticket.status == "cancelled":
        raise ValueError("Ticket already cancelled")

    showtime = ticket.order.showtime

    start_time_str = showtime.time_slot.start_time

    start_time = datetime.strptime(start_time_str, "%H:%M").time()

    show_datetime = datetime.combine(
        showtime.dayshow,
        start_time
    )

    now = datetime.now()

    if now >= show_datetime - timedelta(minutes=5):
        raise ValueError("Cannot cancel ticket within 5 minutes before showtime")

    ticket.status = "cancelled"

    order = ticket.order

    base_price = showtime.ticket_type.base_price if showtime.ticket_type else 0

    active_count = sum(
        1 for t in order.tickets if t.status != "cancelled"
    )

    order.total_amount = base_price * active_count

    db.commit()
    db.refresh(ticket)

    return ticket