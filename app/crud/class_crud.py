from typing import List, Optional
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.class_model import Class, ClassEnrollment
from app.schemas.class_schema import ClassCreate, ClassUpdate, ClassEnrollmentCreate

class CRUDClass(CRUDBase[Class, ClassCreate, ClassUpdate]):
    def get_by_teacher(self, db: Session, *, teacher_id: int) -> List[Class]:
        return db.query(Class).filter(Class.teacher_id == teacher_id, Class.is_active == True).all()
    
    def get_by_subject(self, db: Session, *, subject_id: int) -> List[Class]:
        return db.query(Class).filter(Class.subject_id == subject_id, Class.is_active == True).all()
    
    def get_by_grade_level(self, db: Session, *, grade_level: int) -> List[Class]:
        return db.query(Class).filter(Class.grade_level == grade_level, Class.is_active == True).all()
    
    def get_active_classes(self, db: Session, *, skip: int = 0, limit: int = 100) -> List[Class]:
        return db.query(Class).filter(Class.is_active == True).offset(skip).limit(limit).all()

class CRUDClassEnrollment(CRUDBase[ClassEnrollment, ClassEnrollmentCreate, ClassEnrollmentCreate]):
    def get_by_student(self, db: Session, *, student_id: int) -> List[ClassEnrollment]:
        return db.query(ClassEnrollment).filter(
            ClassEnrollment.student_id == student_id, 
            ClassEnrollment.is_active == True
        ).all()
    
    def get_by_class(self, db: Session, *, class_id: int) -> List[ClassEnrollment]:
        return db.query(ClassEnrollment).filter(
            ClassEnrollment.class_id == class_id, 
            ClassEnrollment.is_active == True
        ).all()
    
    def get_enrollment(self, db: Session, *, student_id: int, class_id: int) -> Optional[ClassEnrollment]:
        return db.query(ClassEnrollment).filter(
            ClassEnrollment.student_id == student_id,
            ClassEnrollment.class_id == class_id,
            ClassEnrollment.is_active == True
        ).first()

class_crud = CRUDClass(Class)
class_enrollment = CRUDClassEnrollment(ClassEnrollment) 