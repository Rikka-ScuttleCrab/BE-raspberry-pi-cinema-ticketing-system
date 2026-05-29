from pydantic import BaseModel


class PosterSchema(BaseModel):
    name: str
    path: str

    class Config:
        from_attributes = True