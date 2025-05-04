from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr
    full_name: str | None = None

class UserCreate(UserBase):
    password: str
    role: str = "student"
    
    @field_validator("password")
    def validate_password(cls, value):
        if len(value) < 12:
            raise ValueError("Password must be at least 12 characters")
        return value

class UserUpdate(UserBase):
    password: Optional[str] = None

class UserOut(UserBase):
    id: str
    role: str
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True