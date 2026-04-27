from sqlalchemy.orm import Session
from models.tickets.ticket import Ticket

def get_tickets_by_order_service(db: Session, order_id: int):
    tickets = (
        db.query(Ticket)
        .filter(Ticket.order_id == order_id)
        .all()
    )

    if not tickets:
        return []

    result = []
    for t in tickets:
        order = t.order
        showtime = order.showtime
        movie = showtime.movie
        room = showtime.theater_room
        seat = t.seat
        time_slot = showtime.time_slot

        result.append({
            "id": t.id,
            "movie_title": movie.title,
            "show_date": showtime.dayshow,
            "start_time": time_slot.start_time,
            "theater_room_name": room.name,
            "seat_name": f"{seat.seat_row}{seat.seat_number}",
            "created_at": order.create_at.strftime("%d/%m/%Y %H:%M:%S ")
        })

    return result