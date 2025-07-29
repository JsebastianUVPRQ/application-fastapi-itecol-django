from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Text
from sqlalchemy.orm import relationship
from app.db.base import Base, TimestampMixin

class Grade(Base, TimestampMixin):
    __tablename__ = "grades"
    
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    class_id = Column(Integer, ForeignKey("classes.id"), nullable=False)
    grade_type = Column(String(50), nullable=False)  # "examen", "tarea", "proyecto", etc.
    grade_value = Column(Float, nullable=False)  # 0.0 - 10.0
    max_grade = Column(Float, default=10.0)
    comments = Column(Text)
    graded_date = Column(DateTime, nullable=False)
    
    # Relaciones
    student = relationship("Student", back_populates="grades")
    class_ = relationship("Class", back_populates="grades")
    
    def __repr__(self):
        return f"<Grade(student_id={self.student_id}, grade={self.grade_value})>" 