from sqlalchemy import Column, Integer, ForeignKey, String, Date, Text, CHAR, Boolean
from sqlalchemy.orm import relationship
from data.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    day_create = Column(Date, nullable = False)
    role_id = Column(CHAR(64), ForeignKey('roles.id'), nullable=False)
    username = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    refresh_token =Column(Text)
    day_update = Column(Date)
    working=Column(Boolean, nullable=False, default=1)
    
    
    role = relationship("Role", back_populates="users")