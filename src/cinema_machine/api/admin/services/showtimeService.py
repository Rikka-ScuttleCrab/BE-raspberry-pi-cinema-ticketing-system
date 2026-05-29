from sqlalchemy.orm import Session, joinedload
from datetime import datetime
from models.theaters.showtime import Showtime
from models.movies.movie import Movie
from models.theaters.timeslot import TimeSlot
from models.tickets.type import TicketType
from models.theaters.theaterroom import TheaterRoom

def get_all_showtimes_service(db: Session, page: int = 1, page_size: int = 30):

    offset = (page - 1) * page_size

    total = db.query(Showtime).count()

    showtimes = (
        db.query(Showtime)
        .options(
            joinedload(Showtime.movie),
            joinedload(Showtime.time_slot),
            joinedload(Showtime.ticket_type),
            joinedload(Showtime.theater_room)
        )
        .order_by(Showtime.id.desc())
        .offset(offset)
        .limit(page_size)
        .all()
    )

    items = []

    for s in showtimes:
        items.append({
            "id": s.id,
            "movie_id": s.movie_id,
            "movie_title": s.movie.title if s.movie else None,
            "theater_room_id": s.theater_room_id,
            "dayshow": s.dayshow,
            "start_time": s.time_slot.start_time if s.time_slot else None,
            "ticket_type": s.ticket_type.name if s.ticket_type else None
        })

    return {
        "items": items,
        "total": total
    }
    

def create_showtime_service(db: Session, data):

    now = datetime.now()
    today = now.date()
    current_time = now.time()

    # ❗ không cho quá khứ
    if data.dayshow < today:
        raise ValueError("Cannot create showtime in the past")

    timeslot = db.query(TimeSlot).filter(TimeSlot.id == data.time_slot_id).first()
    if not timeslot:
        raise ValueError("TimeSlot not found")

    # check giờ hôm nay
    if data.dayshow == today:
        slot_time = datetime.strptime(timeslot.start_time, "%H:%M").time()
        if slot_time <= current_time:
            raise ValueError("Cannot create showtime with past time")

    # ❗ validate room
    room = db.query(TheaterRoom).filter(
        TheaterRoom.id == data.theater_room_id
    ).first()

    if not room:
        raise ValueError("TheaterRoom not found")

    # ❗ check trùng theo ROOM
    existed = db.query(Showtime).filter(
        Showtime.theater_room_id == data.theater_room_id,
        Showtime.dayshow == data.dayshow,
        Showtime.time_slot_id == data.time_slot_id
    ).first()

    if existed:
        raise ValueError("Showtime already exists in this room")

    # validate khác
    movie = db.query(Movie).filter(Movie.id == data.movie_id).first()
    if not movie:
        raise ValueError("Movie not found")

    if data.dayshow < movie.release_date:

        raise ValueError(
            "Ngày chiếu nhỏ hơn ngày khởi chiếu của phim"
        )

    if data.dayshow > movie.end_date:

        raise ValueError(
            "Ngày chiếu vượt quá ngày kết thúc của phim"
        )
    if data.dayshow < today:

        raise ValueError(
            "Không thể tạo suất chiếu trong quá khứ"
        )
    ticket = db.query(TicketType).filter(
        TicketType.id == data.ticket_type_id
    ).first()

    if not ticket:
        raise ValueError("TicketType not found")

    showtime = Showtime(
        movie_id=data.movie_id,
        theater_room_id=data.theater_room_id,
        time_slot_id=data.time_slot_id,
        ticket_type_id=data.ticket_type_id,
        dayshow=data.dayshow
    )

    db.add(showtime)
    db.commit()
    db.refresh(showtime)

    return showtime


def update_showtime_service(db: Session, showtime_id: int, data):

    showtime = db.query(Showtime).filter(Showtime.id == showtime_id).first()

    if not showtime:
        return None

    update_data = data.model_dump(exclude_unset=True)

    movie_id = update_data.get("movie_id", showtime.movie_id)
    theater_room_id = update_data.get("theater_room_id", showtime.theater_room_id)
    dayshow = update_data.get("dayshow", showtime.dayshow)
    time_slot_id = update_data.get("time_slot_id", showtime.time_slot_id)

    # ❗ check trùng theo ROOM
    existed = db.query(Showtime).filter(
        Showtime.theater_room_id == theater_room_id,
        Showtime.dayshow == dayshow,
        Showtime.time_slot_id == time_slot_id,
        Showtime.id != showtime_id
    ).first()

    if existed:
        raise ValueError("Suất chiếu đã tồn tại trong phòng này")

    now = datetime.now()
    today = now.date()
    current_time = now.time()

    if dayshow < today:
        raise ValueError("Cannot update to past showtime")

    timeslot = db.query(TimeSlot).filter(TimeSlot.id == time_slot_id).first()
    if not timeslot:
        raise ValueError("TimeSlot not found")

    if dayshow == today:
        slot_time = datetime.strptime(timeslot.start_time, "%H:%M").time()
        if slot_time <= current_time:
            raise ValueError("Cannot update to past time")

    # update field
    for key, value in update_data.items():
        setattr(showtime, key, value)

    db.commit()
    db.refresh(showtime)

    return showtime