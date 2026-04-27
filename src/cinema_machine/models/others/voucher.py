from sqlalchemy import Column, Integer, ForeignKey, String, Date
from sqlalchemy.orm import relationship
from data.database import Base

class Voucher(Base):
    __tablename__ = 'vouchers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    voucher_code = Column(String(100), nullable=False)
    voucher_value = Column(String(100), nullable=False)
    voucher_exp = Column(Date, nullable = False)
    
    orders = relationship("Order", back_populates="voucher")