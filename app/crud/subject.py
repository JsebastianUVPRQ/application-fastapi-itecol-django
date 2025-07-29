from typing import List, Optional
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.subject import Subject
from app.schemas.subject import SubjectCreate, SubjectUpdate

class CRUDSubject(CRUDBase[Subject, SubjectCreate, SubjectUpdate]):
    def get_by_code(self, db: Session, *, code: str) -> Optional[Subject]:
        return db.query(Subject).filter(Subject.code == code).first()
    
    def get_by_grade_level(self, db: Session, *, grade_level: int) -> List[Subject]:
        return db.query(Subject).filter(Subject.grade_level == grade_level, Subject.is_active == True).all()
    
    def get_active_subjects(self, db: Session, *, skip: int = 0, limit: int = 100) -> List[Subject]:
        return db.query(Subject).filter(Subject.is_active == True).offset(skip).limit(limit).all()

subject = CRUDSubject(Subject) 