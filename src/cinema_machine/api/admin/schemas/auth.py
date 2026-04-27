from pydantic import BaseModel, EmailStr
from typing import Optional


class AuthResponse(BaseModel):
    id: int
    username: str
    role_name: str
    email: EmailStr
    working: bool 
    
    class Config:
        from_attributes = True

class RoleCreate(BaseModel):
    role_name: str

class SignupRequest(BaseModel):
    username: str
    email: EmailStr
    password: str

class UpdateUserRequest(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    role_name: Optional[str] = None
    working: Optional[bool] = None