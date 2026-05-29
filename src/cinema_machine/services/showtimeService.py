from datetime import datetime, date
from sqlalchemy.orm import Session, joinedload
from models.theaters.showtime import Showtime
from models.theaters.theaterroom import TheaterRoom
from models.tickets.order import Order

from models.tickets.ticket import Ticket
from models.theaters.seat import Seat

def get_today_showtimes_with_reserved_seats(db: Session, movie_id: int):
    now = datetime.now()
    today = date.today()

    showtimes = (
        db.query(Showtime)
        .options(
            joinedload(Showtime.time_slot),
            joinedload(Showtime.theater_room),
            joinedload(Showtime.ticket_type)
        )
        .filter(
            Showtime.movie_id == movie_id,
            Showtime.dayshow == today
        )
        .all()
    )

    result = []

    for s in showtimes:
        try:
            start_time_obj = datetime.strptime(s.time_slot.start_time, "%H:%M").time()
            show_datetime = datetime.combine(s.dayshow, start_time_obj)
        except Exception:
            continue

        if show_datetime > now:
            reserved_seats = (
                db.query(Seat)
                .join(Ticket, Ticket.seat_id == Seat.id)
                .join(Order, Ticket.order_id == Order.id)
                .filter(
                    Order.showtime_id == s.id,
                    Ticket.status.in_(["USED","CONFIRMED"])
                )
                .all()
            )

            # Gán trực tiếp ticket_type
            ticket_data = None
            if s.ticket_type:
                ticket_data = {
                    "id": s.ticket_type.id,
                    "name": s.ticket_type.name,
                    "base_price": s.ticket_type.base_price
                }

            result.append({
                "id": s.id,
                "start_time": s.time_slot.start_time,
                "theater_room_id": s.theater_room.id,
                "theater_room_name": s.theater_room.name,
                "ticket_type": ticket_data,
                "reserved_seats": [
                    {
                        "id": seat.id,
                        "seat_row": seat.seat_row,
                        "seat_number": seat.seat_number
                    } for seat in reserved_seats
                ]
            })

    return result