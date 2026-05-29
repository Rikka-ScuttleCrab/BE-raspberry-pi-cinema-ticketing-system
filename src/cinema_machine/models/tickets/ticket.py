from sqlalchemy import Column, Integer, ForeignKey,String
from sqlalchemy.orm import relationship
from data.database import Base

class Ticket(Base):
    __tablename__ = 'tickets'
    id = Column(Integer, primary_key=True, autoincrement=True)
    seat_id = Column(Integer, ForeignKey('seats.id'), nullable=False)
    order_id = Column(Integer, ForeignKey('orders.id'))
    status = Column(String(50), default="ACTIVE")
    
    order = relationship("Order", back_populates="tickets")
    seat = relationship("Seat", back_populates="tickets")