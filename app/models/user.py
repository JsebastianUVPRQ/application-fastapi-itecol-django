from sqlalchemy import Column, String, Boolean, ForeignKey
from .base import BaseModel

class User(BaseModel):
    __tablename__ = "users"
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(255))
    is_active = Column(Boolean, default=True)
    role = Column(String(50), default="student")  # student, teacher, admin

class TeacherStudentAssociation(BaseModel):
    __tablename__ = "teacher_student_association"
    teacher_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    student_id = Column(Integer, ForeignKey("users.id"), nullable=False)