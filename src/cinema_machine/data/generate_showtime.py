from datetime import date, timedelta
import random

TOTAL_SHOWTIMES = 2000

movies = list(range(1, 12))
animation_movies = [3, 7, 10]
IMAX_MOVIE = 5

normal_rooms = [1, 2, 3, 4]
imax_rooms = [5, 6]

time_slots = [
    800, 915, 1030, 1145, 1300, 1415,
    1530, 1645, 1800, 1915, 2030, 2145, 2300
]

start_date = date.today()
days = [start_date + timedelta(days=i) for i in range(30)]

showtimes = []
used_slots = set()         # (room, ts, day)
used_movie_slots = set()   # (movie, ts, day)

# ================= TICKET =================
TICKET_2D_SUB = 1
TICKET_2D_DUB = 2
TICKET_IMAX = 5

def get_normal_ticket(movie):
    if movie in animation_movies:
        return random.choice([TICKET_2D_SUB, TICKET_2D_DUB])
    return TICKET_2D_SUB

def add_show(movie, room, ts, d, ticket):
    key1 = (room, ts, d)
    key2 = (movie, ts, d)

    if key1 in used_slots:
        return False
    if key2 in used_movie_slots:
        return False

    used_slots.add(key1)
    used_movie_slots.add(key2)
    showtimes.append((movie, room, ticket, ts, d))
    return True

# ================= PHASE 1 =================
for d in days:

    # IMAX: đúng 5 suất/ngày, không trùng giờ
    imax_slots = random.sample(time_slots, 5)
    for ts in imax_slots:
        room = random.choice(imax_rooms)
        add_show(IMAX_MOVIE, room, ts, d, TICKET_IMAX)

    # phim thường: ≥ 4 suất
    for movie in movies:
        if movie == IMAX_MOVIE:
            continue

        slots = random.sample(time_slots, 4)
        for ts in slots:
            room = random.choice(normal_rooms)
            add_show(movie, room, ts, d, get_normal_ticket(movie))

# ================= PHASE 2 =================
all_slots = [
    (r, ts, d)
    for d in days
    for r in normal_rooms + imax_rooms
    for ts in time_slots
]

random.shuffle(all_slots)

for r, ts, d in all_slots:
    if len(showtimes) >= TOTAL_SHOWTIMES:
        break

    if (r, ts, d) in used_slots:
        continue

    # ===== IMAX =====
    if r in imax_rooms:
        # đếm số suất IMAX trong ngày
        imax_count_today = sum(
            1 for m, rr, _, _, dd in showtimes
            if dd == d and rr in imax_rooms
        )

        if imax_count_today >= 5:
            continue  # không cho vượt 5 suất/ngày

        movie = IMAX_MOVIE
        ticket = TICKET_IMAX

    # ===== phòng thường =====
    else:
        movie = random.choice([m for m in movies if m != IMAX_MOVIE])
        ticket = get_normal_ticket(movie)

    add_show(movie, r, ts, d, ticket)

# ================= EXPORT =================
values = [
    f"({m},{r},{t},{ts},'{d}')"
    for m, r, t, ts, d in showtimes
]

sql = """INSERT INTO showtimes(movie_id, theater_room_id, ticket_type_id, time_slot_id, dayshow)
VALUES
"""
sql += ",\n".join(values) + ";"

with open("src/cinema_machine/resource/sql/showtimes.sql", "w", encoding="utf-8") as f:
    f.write(sql)

print(f"✅ Done: {len(showtimes)} showtimes")