from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Text, Float
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class TimestampMixin:
    """Mixin para agregar timestamps a los modelos"""
    created_at = Column(DateTime, default=datetime.now(datetime.UTC), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(datetime.UTC), onupdate=datetime.now(datetime.UTC), nullable=False)
    
# class BaseModel(Base, TimestampMixin):