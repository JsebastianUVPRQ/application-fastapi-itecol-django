from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.db.base import Base, TimestampMixin

class Class(Base, TimestampMixin):
    __tablename__ = "classes"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    subject_id = Column(Integer, ForeignKey("subjects.id"), nullable=False)
    teacher_id = Column(Integer, ForeignKey("teachers.id"), nullable=False)
    grade_level = Column(Integer, nullable=False)  # 1-6 para primaria
    schedule = Column(String(100))  # "Lunes 8:00-9:00"
    room = Column(String(20))
    max_students = Column(Integer, default=30)
    is_active = Column(Boolean, default=True)
    
    # Relaciones
    subject = relationship("Subject", back_populates="classes")
    teacher = relationship("Teacher", back_populates="classes")
    enrollments = relationship("ClassEnrollment", back_populates="class_")
    grades = relationship("Grade", back_populates="class_")
    
    def __repr__(self):
        return f"<Class(id={self.id}, name='{self.name}')>"

class ClassEnrollment(Base, TimestampMixin):
    __tablename__ = "class_enrollments"
    
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    class_id = Column(Integer, ForeignKey("classes.id"), nullable=False)
    enrollment_date = Column(DateTime, nullable=False)
    is_active = Column(Boolean, default=True)
    
    # Relaciones
    student = relationship("Student", back_populates="enrollments")
    class_ = relationship("Class", back_populates="enrollments")
    
    def __repr__(self):
        return f"<ClassEnrollment(student_id={self.student_id}, class_id={self.class_id})>" 