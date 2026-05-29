from pydantic import BaseModel

class TrailerSchema(BaseModel):
    name: str
    path: str

    class Config:
        from_attributes = True