from sqlalchemy import Column, Integer, String, Date, Boolean, Text
from sqlalchemy.orm import relationship
from app.db.base import Base, TimestampMixin

class Student(Base, TimestampMixin):
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(String(20), unique=True, index=True, nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, index=True)
    phone = Column(String(20))
    date_of_birth = Column(Date)
    address = Column(Text)
    grade_level = Column(Integer, nullable=False)  # 1-6 para primaria
    is_active = Column(Boolean, default=True)
    
    # Relaciones
    enrollments = relationship("ClassEnrollment", back_populates="student")
    grades = relationship("Grade", back_populates="student")
    
    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.first_name} {self.last_name}')>" 