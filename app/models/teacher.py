from sqlalchemy import Column, Integer, String, Date, Boolean, Text
from sqlalchemy.orm import relationship
from app.db.base import Base, TimestampMixin

class Teacher(Base, TimestampMixin):
    __tablename__ = "teachers"
    
    id = Column(Integer, primary_key=True, index=True)
    teacher_id = Column(String(20), unique=True, index=True, nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    phone = Column(String(20))
    date_of_birth = Column(Date)
    address = Column(Text)
    specialization = Column(String(100))  # Materia principal
    is_active = Column(Boolean, default=True)
    
    # Relaciones
    classes = relationship("Class", back_populates="teacher")
    
    def __repr__(self):
        return f"<Teacher(id={self.id}, name='{self.first_name} {self.last_name}')>" 