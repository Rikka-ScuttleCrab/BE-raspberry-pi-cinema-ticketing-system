from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from data.database import Base

class Showtime(Base):
    __tablename__ = 'showtimes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    movie_id = Column(Integer, ForeignKey('movies.id'), nullable=False)
    theater_room_id = Column(Integer, ForeignKey('theater_rooms.id'), nullable=False)
    time_slot_id = Column(Integer, ForeignKey('time_slots.id'), nullable=False)
    ticket_type_id = Column(Integer, ForeignKey('ticket_types.id'), nullable=False)
    dayshow = Column(Date, nullable=False)

    movie = relationship("Movie", back_populates="showtimes")
    theater_room = relationship("TheaterRoom", back_populates="showtimes")
    time_slot = relationship("TimeSlot", back_populates="showtimes")
    ticket_type = relationship("TicketType", back_populates="showtimes")
    orders = relationship("Order", back_populates="showtime")