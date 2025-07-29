from typing import List, Optional
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.student import Student
from app.schemas.student import StudentCreate, StudentUpdate

class CRUDStudent(CRUDBase[Student, StudentCreate, StudentUpdate]):
    def get_by_student_id(self, db: Session, *, student_id: str) -> Optional[Student]:
        return db.query(Student).filter(Student.student_id == student_id).first()
    
    def get_by_email(self, db: Session, *, email: str) -> Optional[Student]:
        return db.query(Student).filter(Student.email == email).first()
    
    def get_by_grade_level(self, db: Session, *, grade_level: int) -> List[Student]:
        return db.query(Student).filter(Student.grade_level == grade_level, Student.is_active == True).all()
    
    def get_active_students(self, db: Session, *, skip: int = 0, limit: int = 100) -> List[Student]:
        return db.query(Student).filter(Student.is_active == True).offset(skip).limit(limit).all()

student = CRUDStudent(Student) 