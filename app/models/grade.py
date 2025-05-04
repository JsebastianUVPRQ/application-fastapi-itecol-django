from sqlalchemy import Column, Float, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from models.base import BaseModel

class Grade(BaseModel):
    __tablename__ = "grades"
    
    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    classroom_id = Column(UUID(as_uuid=True), ForeignKey("classrooms.id"), nullable=False)
    subject = Column(Text, nullable=False)
    score = Column(Float, nullable=False)
    comments = Column(Text)
    
    __table_args__ = (
        Index('ix_grade_student_subject', 'student_id', 'subject', unique=True),
    )