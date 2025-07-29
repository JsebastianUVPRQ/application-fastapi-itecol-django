from typing import List, Optional
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.grade import Grade
from app.schemas.grade import GradeCreate, GradeUpdate

class CRUDGrade(CRUDBase[Grade, GradeCreate, GradeUpdate]):
    def get_by_student(self, db: Session, *, student_id: int) -> List[Grade]:
        return db.query(Grade).filter(Grade.student_id == student_id).all()
    
    def get_by_class(self, db: Session, *, class_id: int) -> List[Grade]:
        return db.query(Grade).filter(Grade.class_id == class_id).all()
    
    def get_by_student_and_class(self, db: Session, *, student_id: int, class_id: int) -> List[Grade]:
        return db.query(Grade).filter(
            Grade.student_id == student_id,
            Grade.class_id == class_id
        ).all()
    
    def get_by_grade_type(self, db: Session, *, class_id: int, grade_type: str) -> List[Grade]:
        return db.query(Grade).filter(
            Grade.class_id == class_id,
            Grade.grade_type == grade_type
        ).all()
    
    def get_student_average(self, db: Session, *, student_id: int, class_id: int) -> Optional[float]:
        grades = self.get_by_student_and_class(db, student_id=student_id, class_id=class_id)
        if not grades:
            return None
        total = sum(grade.grade_value for grade in grades)
        return total / len(grades)

grade = CRUDGrade(Grade) 