from sqlalchemy import Column, Integer, String, Text, Boolean
from sqlalchemy.orm import relationship
from app.db.base import Base, TimestampMixin

class Subject(Base, TimestampMixin):
    __tablename__ = "subjects"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    code = Column(String(10), unique=True, nullable=False)
    description = Column(Text)
    grade_level = Column(Integer, nullable=False)  # 1-6 para primaria
    is_active = Column(Boolean, default=True)
    
    # Relaciones
    classes = relationship("Class", back_populates="subject")
    
    def __repr__(self):
        return f"<Subject(id={self.id}, name='{self.name}')>" 