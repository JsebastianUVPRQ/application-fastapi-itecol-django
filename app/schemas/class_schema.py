from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class ClassBase(BaseModel):
    name: str
    subject_id: int
    teacher_id: int
    grade_level: int
    schedule: Optional[str] = None
    room: Optional[str] = None
    max_students: int = 30
    is_active: bool = True

class ClassCreate(ClassBase):
    pass

class ClassUpdate(BaseModel):
    name: Optional[str] = None
    subject_id: Optional[int] = None
    teacher_id: Optional[int] = None
    grade_level: Optional[int] = None
    schedule: Optional[str] = None
    room: Optional[str] = None
    max_students: Optional[int] = None
    is_active: Optional[bool] = None

class ClassResponse(ClassBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class ClassEnrollmentBase(BaseModel):
    student_id: int
    class_id: int
    enrollment_date: datetime
    is_active: bool = True

class ClassEnrollmentCreate(ClassEnrollmentBase):
    pass

class ClassEnrollmentResponse(ClassEnrollmentBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True 