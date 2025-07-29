from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.crud.student import student
from app.schemas.student import StudentCreate, StudentUpdate, StudentResponse
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
def create_student(
    *,
    db: Session = Depends(get_db),
    student_in: StudentCreate,
):
    """
    Crear un nuevo estudiante.
    """
    # Verificar si el student_id ya existe
    existing_student = student.get_by_student_id(db, student_id=student_in.student_id)
    if existing_student:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ya existe un estudiante con este ID"
        )
    
    # Verificar si el email ya existe
    if student_in.email:
        existing_email = student.get_by_email(db, email=student_in.email)
        if existing_email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ya existe un estudiante con este email"
            )
    
    student_obj = student.create(db, obj_in=student_in)
    return student_obj

@router.get("/", response_model=List[StudentResponse])
def read_students(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    grade_level: Optional[int] = None,
):
    """
    Obtener lista de estudiantes.
    """
    if grade_level:
        students = student.get_by_grade_level(db, grade_level=grade_level)
    else:
        students = student.get_active_students(db, skip=skip, limit=limit)
    return students

@router.get("/{student_id}", response_model=StudentResponse)
def read_student(
    *,
    db: Session = Depends(get_db),
    student_id: int,
):
    """
    Obtener un estudiante por ID.
    """
    student_obj = student.get(db, id=student_id)
    if not student_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Estudiante no encontrado"
        )
    return student_obj

@router.put("/{student_id}", response_model=StudentResponse)
def update_student(
    *,
    db: Session = Depends(get_db),
    student_id: int,
    student_in: StudentUpdate,
):
    """
    Actualizar un estudiante.
    """
    student_obj = student.get(db, id=student_id)
    if not student_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Estudiante no encontrado"
        )
    
    # Verificar si el nuevo student_id ya existe
    if student_in.student_id and student_in.student_id != student_obj.student_id:
        existing_student = student.get_by_student_id(db, student_id=student_in.student_id)
        if existing_student:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ya existe un estudiante con este ID"
            )
    
    # Verificar si el nuevo email ya existe
    if student_in.email and student_in.email != student_obj.email:
        existing_email = student.get_by_email(db, email=student_in.email)
        if existing_email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ya existe un estudiante con este email"
            )
    
    student_obj = student.update(db, db_obj=student_obj, obj_in=student_in)
    return student_obj

@router.delete("/{student_id}")
def delete_student(
    *,
    db: Session = Depends(get_db),
    student_id: int,
):
    """
    Eliminar un estudiante (marcar como inactivo).
    """
    student_obj = student.get(db, id=student_id)
    if not student_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Estudiante no encontrado"
        )
    
    # Marcar como inactivo en lugar de eliminar
    student_obj.is_active = False
    db.commit()
    return {"message": "Estudiante eliminado exitosamente"} 