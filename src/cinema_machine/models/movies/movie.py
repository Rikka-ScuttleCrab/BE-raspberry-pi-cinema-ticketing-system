from datetime import date
from sqlalchemy import Column, Integer, String, Text, Date, Boolean
from sqlalchemy.orm import relationship
from data.database import Base
from models.association import movie_category_association

class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    age_rating = Column(String(10), nullable=False) # do_tuoi
    actors = Column(Text)
    duration_min = Column(Integer, nullable=False) # thoi_luong_phim
    description = Column(Text)
    release_date = Column(Date)
    end_date = Column(Date)

    categories = relationship("Category", 
        secondary=movie_category_association, 
        back_populates="movies"
    )
    
    posters = relationship("Poster", back_populates="movie")
    trailers = relationship("Trailer", back_populates="movie")
    showtimes = relationship("Showtime", back_populates="movie")
    
    @property
    def status(self):
        today = date.today()

        if today < self.release_date:
            return "Sắp chiếu"
        elif self.release_date <= today <= self.end_date:
            return "Đang chiếu"
        else:
            return "Ngưng chiếu"