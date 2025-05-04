from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies.database import get_db
from dependencies.auth import get_current_active_user
from schemas.classroom import ClassroomCreate, ClassroomOut
from services.classroom_service import create_classroom, get_classroom

router = APIRouter()

@router.post("/", response_model=ClassroomOut)
def create_new_classroom(
    classroom: ClassroomCreate,
    db: Session = Depends(get_db),
    current_user: UserOut = Depends(get_current_active_user)
):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")
    return create_classroom(db=db, classroom=classroom)

@router.get("/{classroom_id}", response_model=ClassroomOut)
def get_classroom_details(
    classroom_id: int,
    db: Session = Depends(get_db),
    current_user: UserOut = Depends(get_current_active_user)
):
    classroom = get_classroom(db, classroom_id)
    if not classroom:
        raise HTTPException(status_code=404, detail="Classroom not found")
    return classroom