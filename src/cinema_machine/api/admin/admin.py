from fastapi import APIRouter

from api.admin.routes import movie, category, voucher, auth, showtime, ticket

router = APIRouter(prefix="/api/v1/admin", tags=["Admin"])

router.include_router(auth.router)
router.include_router(movie.router)
router.include_router(category.router)
router.include_router(voucher.router)
router.include_router(showtime.router)
router.include_router(ticket.router)