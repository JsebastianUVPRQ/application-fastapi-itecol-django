from sqlalchemy.orm import Session
from models.classroom import Classroom, Enrollment

def create_classroom(db: Session, classroom: ClassroomCreate):
    db_classroom = Classroom(**classroom.dict())
    db.add(db_classroom)
    db.commit()
    db.refresh(db_classroom)
    return db_classroom

def enroll_student(db: Session, student_id: int, classroom_id: int):
    enrollment = Enrollment(student_id=student_id, classroom_id=classroom_id)
    db.add(enrollment)
    db.commit()
    return enrollment