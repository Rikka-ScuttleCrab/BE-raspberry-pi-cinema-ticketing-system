from pydantic import BaseModel
from typing import Optional


class CategoryAdminResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]

    class Config:
        from_attributes = True
        
        
class CategoryCreateAdmin(BaseModel):
    name: str
    description: Optional[str] = None



class CategoryUpdateAdmin(BaseModel):
    name: str
    description: Optional[str] = None