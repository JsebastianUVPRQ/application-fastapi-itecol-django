from sqlalchemy import Column, String, Integer, ForeignKey

class Classroom(BaseModel):
    __tablename__ = "classrooms"
    name = Column(String(100), unique=True, index=True)
    grade_level = Column(String(50))
    teacher_id = Column(Integer, ForeignKey("users.id"))

class Enrollment(BaseModel):
    __tablename__ = "enrollments"
    student_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    classroom_id = Column(Integer, ForeignKey("classrooms.id"), nullable=False)

# --- models/grade.py ---
from sqlalchemy import Column, Float, Text, ForeignKey

class Grade(BaseModel):
    __tablename__ = "grades"
    student_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    classroom_id = Column(Integer, ForeignKey("classrooms.id"), nullable=False)
    subject = Column(String(100), nullable=False)
    score = Column(Float, nullable=False)
    comments = Column(Text)