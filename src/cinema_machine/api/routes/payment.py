from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session
import random

from api.schemas.payment import PaymentCreateRequest, PaymentCreateResponse, PaymentReturnResponse
from api.response import success_response, error_response
from api.deps import get_db
from services.vnpayService import build_vnpay_url, verify_vnpay_return
from services.paymentService import create_payment_invoice, get_payment_invoice_by_order_id, update_payment_invoice

router = APIRouter(prefix="/api/v1/payments", tags=["Payments"])


@router.post("/create", response_model=PaymentCreateResponse)
def create_payment(payment: PaymentCreateRequest, request: Request, db: Session = Depends(get_db)):
    order_id = payment.order_id or str(random.randint(10000000, 99999999))
    amount = payment.amount
    if amount <= 0:
        raise HTTPException(status_code=400, detail='Amount must be greater than 0')

    ip_addr = request.client.host if request.client else '127.0.0.1'

    payment_url = build_vnpay_url(
        order_id=order_id,
        amount=amount,
        ip_addr=ip_addr,
        order_info=payment.order_info,
        order_type=payment.order_type,
        bank_code=payment.bank_code
    )

    invoice = create_payment_invoice(
        db,
        order_id=order_id,
        amount=amount,
        order_info=payment.order_info,
        order_type=payment.order_type,
        bank_code=payment.bank_code,
        ip_addr=ip_addr,
        status='pending'
    )

    return PaymentCreateResponse(order_id=invoice.order_id, payment_url=payment_url, total_amount=invoice.amount)


@router.get("/return", response_model=PaymentReturnResponse)
def payment_return(request: Request, db: Session = Depends(get_db)):
    query = dict(request.query_params)

    verified, result = verify_vnpay_return(query)
    if not verified:
        raise HTTPException(status_code=400, detail=result.get('message', 'Invalid payment signature'))

    order_id = query.get('vnp_TxnRef')
    if not order_id:
        raise HTTPException(status_code=400, detail='Missing order reference')

    invoice = get_payment_invoice_by_order_id(db, order_id)
    if not invoice:
        raise HTTPException(status_code=404, detail='Invoice not found')

    status = 'success' if result['success'] else 'failed'
    update_payment_invoice(
        db,
        order_id=order_id,
        vnp_txn_ref=result.get('transaction_ref'),
        vnp_response_code=result.get('response_code'),
        vnp_transaction_no=query.get('vnp_TransactionNo'),
        vnp_secure_hash=query.get('vnp_SecureHash'),
        vnp_transaction_status=query.get('vnp_TransactionStatus'),
        status=status
    )

    return PaymentReturnResponse(**result)
