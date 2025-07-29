from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class GradeBase(BaseModel):
    student_id: int
    class_id: int
    grade_type: str
    grade_value: float
    max_grade: float = 10.0
    comments: Optional[str] = None
    graded_date: datetime

class GradeCreate(GradeBase):
    pass

class GradeUpdate(BaseModel):
    grade_type: Optional[str] = None
    grade_value: Optional[float] = None
    max_grade: Optional[float] = None
    comments: Optional[str] = None
    graded_date: Optional[datetime] = None

class GradeResponse(GradeBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True 