from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base, TimestampMixin

class ActivityLog(Base, TimestampMixin):
    __tablename__ = "activity_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=True)  # ID del usuario que realizó la acción
    user_type = Column(String(50), nullable=False)  # "teacher", "admin", "student"
    action = Column(String(100), nullable=False)  # "create", "update", "delete", "login", etc.
    resource_type = Column(String(50), nullable=False)  # "student", "class", "grade", etc.
    resource_id = Column(Integer, nullable=True)  # ID del recurso afectado
    description = Column(Text, nullable=False)  # Descripción detallada de la acción
    ip_address = Column(String(45))  # IPv4 o IPv6
    user_agent = Column(Text)  # Información del navegador
    
    def __repr__(self):
        return f"<ActivityLog(action='{self.action}', resource='{self.resource_type}')>" 