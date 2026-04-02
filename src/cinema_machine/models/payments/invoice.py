from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float, Text
from data.database import Base

class PaymentInvoice(Base):
    __tablename__ = 'payment_invoices'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(String(64), nullable=False, unique=True, index=True)
    amount = Column(Float, nullable=False)
    order_info = Column(Text, nullable=True)
    order_type = Column(String(50), nullable=True)
    bank_code = Column(String(20), nullable=True)
    ip_addr = Column(String(45), nullable=True)

    vnp_txn_ref = Column(String(64), nullable=True)
    vnp_response_code = Column(String(5), nullable=True)
    vnp_transaction_no = Column(String(64), nullable=True)
    vnp_secure_hash = Column(String(128), nullable=True)
    vnp_transaction_status = Column(String(20), nullable=True)

    status = Column(String(20), nullable=False, default='pending')

    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
