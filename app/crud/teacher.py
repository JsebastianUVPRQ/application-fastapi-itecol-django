from typing import List, Optional
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.teacher import Teacher
from app.schemas.teacher import TeacherCreate, TeacherUpdate

class CRUDTeacher(CRUDBase[Teacher, TeacherCreate, TeacherUpdate]):
    def get_by_teacher_id(self, db: Session, *, teacher_id: str) -> Optional[Teacher]:
        return db.query(Teacher).filter(Teacher.teacher_id == teacher_id).first()
    
    def get_by_email(self, db: Session, *, email: str) -> Optional[Teacher]:
        return db.query(Teacher).filter(Teacher.email == email).first()
    
    def get_by_specialization(self, db: Session, *, specialization: str) -> List[Teacher]:
        return db.query(Teacher).filter(Teacher.specialization == specialization, Teacher.is_active == True).all()
    
    def get_active_teachers(self, db: Session, *, skip: int = 0, limit: int = 100) -> List[Teacher]:
        return db.query(Teacher).filter(Teacher.is_active == True).offset(skip).limit(limit).all()

teacher = CRUDTeacher(Teacher) 