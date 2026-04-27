from sqlalchemy import Column, String,CHAR
from sqlalchemy.orm import relationship
from data.database import Base

class Role(Base):
    __tablename__ = 'roles'
    id = Column(CHAR(64), primary_key=True)
    role_name = Column(String(100), nullable=False, unique=True)
    
    users = relationship("User", back_populates="role")