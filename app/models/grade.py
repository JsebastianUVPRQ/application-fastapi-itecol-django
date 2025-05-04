# --- models/grade.py ---
from sqlalchemy import Column, Float, Text, ForeignKey

class Grade(BaseModel):
    __tablename__ = "grades"
    student_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    classroom_id = Column(Integer, ForeignKey("classrooms.id"), nullable=False)
    subject = Column(String(100), nullable=False)
    score = Column(Float, nullable=False)
    comments = Column(Text)