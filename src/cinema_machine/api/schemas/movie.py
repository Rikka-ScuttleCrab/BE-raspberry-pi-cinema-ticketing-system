from pydantic import BaseModel, Field
from typing import Optional, List
from api.schemas.category import CategorySchema
from api.schemas.type import TicketTypeSchema
from api.schemas.trailer import TrailerSchema
from api.schemas.poster import PosterSchema

class MovieBase(BaseModel):
    id: int
    title: str
    actors: Optional[str]
    age_rating: Optional[str]
    duration_min: int
    categories: List[str] = Field(default_factory=list)
    description: Optional[str]
    posters: List[PosterSchema] = Field(default_factory=list)
    trailers: List[TrailerSchema] = Field(default_factory=list)
    class Config:
        from_attributes = True


class MovieDetailResponse(BaseModel):

    id: int
    title: str
    actors: Optional[str]
    description: Optional[str]
    age_rating: Optional[str]
    duration_min: int
    status: str

    categories: List[str] = Field(default_factory=list)

    posters: List[PosterSchema] = Field(default_factory=list)
    
    trailers: List[TrailerSchema] = Field(default_factory=list)
    
    class Config:
        from_attributes = True
    