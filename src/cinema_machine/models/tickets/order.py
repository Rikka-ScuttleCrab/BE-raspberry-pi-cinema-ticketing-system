from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, Numeric, func, BIGINT
from sqlalchemy.orm import relationship
from data.database import Base


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, autoincrement=True)

    create_at = Column(DateTime, server_default=func.now())

    showtime_id = Column(Integer, ForeignKey('showtimes.id'), nullable=False)
    voucher_id = Column(Integer, ForeignKey('vouchers.id'))

    guest_name = Column(String(255))
    
    info = Column(String(255))

    total_amount = Column(Numeric(10, 2))

    status = Column(String(50), nullable=False, default="PENDING")

    payment_order_code = Column(BIGINT, unique=True)

    paid_at = Column(DateTime)

    showtime = relationship("Showtime", back_populates="orders")
    tickets = relationship("Ticket", back_populates="order")
    voucher = relationship("Voucher", back_populates="orders")