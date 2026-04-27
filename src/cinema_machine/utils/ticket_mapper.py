from datetime import datetime

def build_ticket_response(ticket, showtime, seat_name):

    return {
        "id": ticket.id,
        "movie_title": showtime.movie.title if showtime.movie else None,
        "show_date": showtime.dayshow,
        "start_time": showtime.time_slot.start_time if showtime.time_slot else None,
        "theater_room_name": showtime.theater_room.name if showtime.theater_room else None,
        "seat_name": seat_name,
        "created_at": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }