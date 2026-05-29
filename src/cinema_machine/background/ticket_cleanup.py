from datetime import datetime, timedelta
from sqlalchemy.orm import Session

from data.database import SessionLocal

from models.tickets.ticket import Ticket
from models.tickets.order import Order
from models.theaters.showtime import Showtime


def cleanup_expired_tickets():

    db: Session = SessionLocal()

    try:

        now = datetime.now()

        # =========================
        # ACTIVE quá 3 phút
        # =========================

        expired_tickets = (
            db.query(Ticket)
            .join(Order, Ticket.order_id == Order.id)
            .filter(
                Ticket.status == "ACTIVE",
                Order.create_at <= now - timedelta(minutes=3)
            )
            .all()
        )

        for ticket in expired_tickets:
            ticket.status = "CANCELLED"

        # =========================
        # ACTIVE nhưng quá giờ chiếu
        # =========================

        active_tickets = (
            db.query(Ticket)
            .join(Order, Ticket.order_id == Order.id)
            .join(Showtime, Order.showtime_id == Showtime.id)
            .filter(
                Ticket.status == "ACTIVE"
            )
            .all()
        )
        if not active_tickets:

            print("No active tickets")

            return
        
        for ticket in active_tickets:

            order = ticket.order
            showtime = order.showtime

            try:

                start_time = datetime.strptime(
                    showtime.time_slot.start_time,
                    "%H:%M"
                ).time()

                show_datetime = datetime.combine(
                    showtime.dayshow,
                    start_time
                )

                if show_datetime <= now:
                    ticket.status = "CANCELLED"

            except Exception:
                continue

        db.commit()

        print("Cleanup completed")

    except Exception as e:

        db.rollback()

        print("Cleanup error:", e)

    finally:
        db.close()