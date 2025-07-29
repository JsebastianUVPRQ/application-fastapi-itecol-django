from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date, datetime

class StudentBase(BaseModel):
    student_id: str
    first_name: str
    last_name: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    date_of_birth: Optional[date] = None
    address: Optional[str] = None
    grade_level: int
    is_active: bool = True

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    student_id: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    date_of_birth: Optional[date] = None
    address: Optional[str] = None
    grade_level: Optional[int] = None
    is_active: Optional[bool] = None

class StudentResponse(StudentBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True 