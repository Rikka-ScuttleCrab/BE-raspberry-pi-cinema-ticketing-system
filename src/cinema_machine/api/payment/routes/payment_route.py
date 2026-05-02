from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from api.payment.schemas.payment import PaymentRequest
from api.deps import get_db
from api.payment.services.payment_service import (
    create_payment_link, 
    get_payment_status_from_payos,
    process_payment_webhook
)


router = APIRouter(prefix="/payment")

@router.post("/create/{order_id}")
def create_payment(order_id: int, body: PaymentRequest, db: Session = Depends(get_db)):
    result = create_payment_link(order_id, body.amount, db)
    return result

@router.get("/status-payos/{order_id}")
def get_status_payos(order_id: int, db: Session = Depends(get_db)):
    return get_payment_status_from_payos(order_id, db)

@router.post("/webhook")
async def payment_webhook(request: Request, db: Session = Depends(get_db)):
    payload = await request.json()
    return process_payment_webhook(payload, db)