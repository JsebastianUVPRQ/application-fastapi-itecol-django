from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date, datetime

class TeacherBase(BaseModel):
    teacher_id: str
    first_name: str
    last_name: str
    email: EmailStr
    phone: Optional[str] = None
    date_of_birth: Optional[date] = None
    address: Optional[str] = None
    specialization: Optional[str] = None
    is_active: bool = True

class TeacherCreate(TeacherBase):
    pass

class TeacherUpdate(BaseModel):
    teacher_id: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    date_of_birth: Optional[date] = None
    address: Optional[str] = None
    specialization: Optional[str] = None
    is_active: Optional[bool] = None

class TeacherResponse(TeacherBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True 