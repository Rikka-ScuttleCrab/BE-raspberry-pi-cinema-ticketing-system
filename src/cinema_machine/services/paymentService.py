from datetime import datetime
from sqlalchemy.orm import Session
from models.payments.invoice import PaymentInvoice


def create_payment_invoice(db: Session, *, order_id: str, amount: float, order_info: str, order_type: str, bank_code: str, ip_addr: str, status: str = 'pending') -> PaymentInvoice:
    invoice = PaymentInvoice(
        order_id=order_id,
        amount=amount,
        order_info=order_info,
        order_type=order_type,
        bank_code=bank_code,
        ip_addr=ip_addr,
        status=status,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    db.add(invoice)
    db.commit()
    db.refresh(invoice)
    return invoice


def get_payment_invoice_by_order_id(db: Session, order_id: str) -> PaymentInvoice | None:
    return db.query(PaymentInvoice).filter(PaymentInvoice.order_id == order_id).first()


def update_payment_invoice(db: Session, order_id: str, **update_fields) -> PaymentInvoice | None:
    invoice = get_payment_invoice_by_order_id(db, order_id)
    if not invoice:
        return None

    for k, v in update_fields.items():
        if hasattr(invoice, k):
            setattr(invoice, k, v)

    invoice.updated_at = datetime.utcnow()
    db.add(invoice)
    db.commit()
    db.refresh(invoice)
    return invoice
