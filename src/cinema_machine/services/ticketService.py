from sqlalchemy.orm import Session
from models.tickets.ticket import Ticket
from models.tickets.order import Order
from models.theaters.showtime import Showtime
from services.qr_service import generate_order_qr
from services.mail_service import send_ticket_email
from sqlalchemy.orm import joinedload

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
        status = t.status
        created_at = t.order.create_at
        paid_at = t.order.paid_at
        result.append({
            "id": t.id,
            "movie_title": movie.title,
            "show_date": showtime.dayshow,
            "start_time": time_slot.start_time,
            "theater_room_name": room.name,
            "seat_name": f"{seat.seat_row}{seat.seat_number}",
            "created_at": created_at,
            "status": status,
            "paid_at": paid_at
        })

    return result


async def send_tickets_service(
    db,
    order_id: int
):

    order = (
        db.query(Order)
        .options(

            joinedload(Order.showtime)
                .joinedload(Showtime.movie),

            joinedload(Order.tickets)
                .joinedload(Ticket.seat)
        )
        .filter(Order.id == order_id)
        .first()
    )

    if not order:
        return {
            "success": False,
            "message": "Order not found"
        }

    # =========================
    # Generate ONE QR
    # =========================

    qr_path = generate_order_qr(order)

    # =========================
    # Seats
    # =========================

    seats = []

    for ticket in order.tickets:

        seats.append(
            f"{ticket.seat.seat_row}"
            f"{ticket.seat.seat_number}"
        )

    seats_text = ", ".join(seats)

    # =========================
    # Email body
    # =========================

    html = f"""
    <h2>Cinema Ticket</h2>

    <p><b>Movie:</b>
    {order.showtime.movie.title}</p>

    <p><b>Seats:</b>
    {seats_text}</p>

    <p><b>Order ID:</b>
    {order.id}</p>

    <p>Please use the attached QR code
    to check in.</p>
    """

    await send_ticket_email(

        email=order.info,

        subject="Cinema Tickets",

        body=html,

        qr_path=qr_path
    )

    return {
        "success": True,
        "message": "Tickets sent successfully"
    }   
    
def verify_ticket_service(
    db,
    order_id: int
):

    order = (
        db.query(Order)
        .options(

            joinedload(Order.tickets)
            .joinedload(Ticket.seat),

            joinedload(Order.showtime)
            .joinedload(Showtime.movie)

        )
        .filter(Order.id == order_id)
        .first()
    )

    # =========================
    # Không tồn tại
    # =========================

    if not order:

        return {
            "success": False,
            "message": "Order not found"
        }

    # =========================
    # CHECK ALL TICKETS
    # =========================

    for ticket in order.tickets:

        # Vé đã dùng
        if ticket.status == "USED":

            return {
                "success": False,
                "message": (
                    f"Ticket {ticket.id} "
                    f"already used"
                )
            }

        # # Vé bị huỷ
        # if ticket.status == "CANCELLED":

        #     return {
        #         "success": False,
        #         "message": (
        #             f"Ticket {ticket.id} "
        #             f"cancelled"
        #         )
        #     }

        # # # Vé không hợp lệ
        # if ticket.status != "CONFIRMED":

        #     return {
        #         "success": False,
        #         "message": (
        #             f"Ticket {ticket.id} "
        #             f"invalid"
        #         )
        #     }

    # =========================
    # UPDATE ALL -> USED
    # =========================

    for ticket in order.tickets:
        ticket.status = "USED"

    db.commit()

    # =========================
    # Seats
    # =========================

    seats = []

    for ticket in order.tickets:

        seats.append(
            f"{ticket.seat.seat_row}"
            f"{ticket.seat.seat_number}"
        )

    # =========================
    # Response
    # =========================

    return {

        "success": True,

        "message": "Check-in success",

        "order": {

            "order_id": order.id,
            "show_date": order.showtime.dayshow,
            "movie": (
                order.showtime
                .movie
                .title
            ),
            "theater_room": order.showtime.theater_room.name,
            
            "seats": seats,

            "total_tickets": len(order.tickets),

            "status": "USED",
            
            "paid_at": order.paid_at
        }
    } 
    