from fastapi import APIRouter

from api.routes import (
    movie,
    showtime,
    theaterroom,
    otp,
    voucher,
    ticket,
    auth,
    order
)

router = APIRouter()

router.include_router(movie.router)
router.include_router(showtime.router)
router.include_router(theaterroom.router)
router.include_router(otp.router)
router.include_router(order.router)
router.include_router(voucher.router)
router.include_router(ticket.router)
router.include_router(auth.router)