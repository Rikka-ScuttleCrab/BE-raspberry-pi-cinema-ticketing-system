from fastapi import APIRouter
from api.payment.routes import payment_route

router = APIRouter()

router.include_router(payment_route.router)