from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date
from api.schemas.poster import PosterSchema
from api.schemas.trailer import TrailerSchema

class MovieAdminResponse(BaseModel):
    id: int
    title: str
    actors: Optional[str]
    age_rating: Optional[str]
    duration_min: int
    description: Optional[str]

    release_date: date
    end_date: date
    status: str

    categories: List[str] = Field(default_factory=list)
    posters: List[PosterSchema] = Field(default_factory=list)
    trailers: List[TrailerSchema] = Field(default_factory=list)

    class Config:
        from_attributes = True
        
        
class MovieCreateAdmin(BaseModel):
    title: str
    age_rating: str
    duration_min: int

    actors: Optional[str] = None
    description: Optional[str] = None
    release_date: Optional[date] = None
    end_date: Optional[date] = None

    poster_path: Optional[str] = None
    poster_name: Optional[str] = None

    trailer_path: Optional[str] = None
    trailer_name: Optional[str] = None


class MovieUpdateAdmin(BaseModel):
    title: Optional[str] = None
    age_rating: Optional[str] = None
    duration_min: Optional[int] = None

    actors: Optional[str] = None
    description: Optional[str] = None
    release_date: Optional[date] = None
    end_date: Optional[date] = None

    poster_path: Optional[str] = None
    trailer_path: Optional[str] = None