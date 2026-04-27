from sqlalchemy import tuple_
from sqlalchemy.orm import Session, joinedload
from datetime import date
from utils.ticket_mapper import build_ticket_response
from models.tickets.order import Order
from models.tickets.ticket import Ticket
from models.theaters.showtime import Showtime
from models.theaters.seat import Seat
from api.schemas.order import OrderRequest

def create_order_service(db: Session, data: OrderRequest):

    showtime = (
        db.query(Showtime)
        .options(
            joinedload(Showtime.movie),
            joinedload(Showtime.time_slot),
            joinedload(Showtime.ticket_type),
            joinedload(Showtime.theater_room)
        )
        .filter(Showtime.id == data.showtime_id)
        .first()
    )

    if not showtime:
        return {"error": "Showtime not found"}

    theater_room_id = showtime.theater_room_id
    requested_seats = list({
    (s.seat_row, s.seat_number) for s in data.seats
    })

    if not requested_seats:
        return {"error": "Seat list is empty"}

    # 2. Query 1 lần
    seats = (
        db.query(Seat)
        .filter(
            Seat.theater_room_id == theater_room_id,
            tuple_(Seat.seat_row, Seat.seat_number).in_(requested_seats)
        )
        .all()
    )

    # 3. Check ghế không tồn tại
    found_seats = {(s.seat_row, s.seat_number) for s in seats}
    missing_seats = set(requested_seats) - found_seats

    if missing_seats:
        missing_str = ", ".join([f"{r}{n}" for r, n in missing_seats])
        return {"error": f"Seats not found: {missing_str}"}

    # 4. Map + list id
    seat_map = {
        s.id: f"{s.seat_row}{s.seat_number}"
        for s in seats
    }

    target_seat_ids = [s.id for s in seats]

    existing_tickets = (
        db.query(Ticket)
        .join(Order)
        .filter(
            Order.showtime_id == data.showtime_id,
            Ticket.seat_id.in_(target_seat_ids)
        )
        .all()
    )

    if existing_tickets:
        booked_seat_ids = [t.seat_id for t in existing_tickets]
        booked_names = [seat_map[sid] for sid in booked_seat_ids if sid in seat_map]

        return {"error": f"Seats already booked: {', '.join(booked_names)}"}

    base_price = float(showtime.ticket_type.base_price) if showtime.ticket_type else 0
    total_amount = base_price * len(target_seat_ids)

    try:
        new_order = Order(
            showtime_id=data.showtime_id,
            voucher_id=data.voucher_id,
            guest_name=data.guest_name,
            info=data.info,
            total_amount=total_amount
        )
        db.add(new_order)
        db.flush()

        tickets_response = []

        for s_id in target_seat_ids:
            new_ticket = Ticket(
                seat_id=s_id,
                order_id=new_order.id
            )
            db.add(new_ticket)
            db.flush()

            tickets_response.append(
                build_ticket_response(
                    ticket=new_ticket,
                    showtime=showtime,
                    seat_name=seat_map[s_id]
                )
            )

        db.commit()

        return {
            "order_id": new_order.id,
            "total_amount": total_amount,
            "tickets": tickets_response
        }

    except Exception as e:
        db.rollback()
        return {"error": str(e)}