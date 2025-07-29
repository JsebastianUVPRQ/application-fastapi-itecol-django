from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.crud.teacher import teacher
from app.schemas.teacher import TeacherCreate, TeacherUpdate, TeacherResponse
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=TeacherResponse, status_code=status.HTTP_201_CREATED)
def create_teacher(
    *,
    db: Session = Depends(get_db),
    teacher_in: TeacherCreate,
):
    """
    Crear un nuevo profesor.
    """
    # Verificar si el teacher_id ya existe
    existing_teacher = teacher.get_by_teacher_id(db, teacher_id=teacher_in.teacher_id)
    if existing_teacher:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ya existe un profesor con este ID"
        )
    
    # Verificar si el email ya existe
    existing_email = teacher.get_by_email(db, email=teacher_in.email)
    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ya existe un profesor con este email"
        )
    
    teacher_obj = teacher.create(db, obj_in=teacher_in)
    return teacher_obj

@router.get("/", response_model=List[TeacherResponse])
def read_teachers(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    specialization: Optional[str] = None,
):
    """
    Obtener lista de profesores.
    """
    if specialization:
        teachers = teacher.get_by_specialization(db, specialization=specialization)
    else:
        teachers = teacher.get_active_teachers(db, skip=skip, limit=limit)
    return teachers

@router.get("/{teacher_id}", response_model=TeacherResponse)
def read_teacher(
    *,
    db: Session = Depends(get_db),
    teacher_id: int,
):
    """
    Obtener un profesor por ID.
    """
    teacher_obj = teacher.get(db, id=teacher_id)
    if not teacher_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profesor no encontrado"
        )
    return teacher_obj

@router.put("/{teacher_id}", response_model=TeacherResponse)
def update_teacher(
    *,
    db: Session = Depends(get_db),
    teacher_id: int,
    teacher_in: TeacherUpdate,
):
    """
    Actualizar un profesor.
    """
    teacher_obj = teacher.get(db, id=teacher_id)
    if not teacher_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profesor no encontrado"
        )
    
    # Verificar si el nuevo teacher_id ya existe
    if teacher_in.teacher_id and teacher_in.teacher_id != teacher_obj.teacher_id:
        existing_teacher = teacher.get_by_teacher_id(db, teacher_id=teacher_in.teacher_id)
        if existing_teacher:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ya existe un profesor con este ID"
            )
    
    # Verificar si el nuevo email ya existe
    if teacher_in.email and teacher_in.email != teacher_obj.email:
        existing_email = teacher.get_by_email(db, email=teacher_in.email)
        if existing_email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ya existe un profesor con este email"
            )
    
    teacher_obj = teacher.update(db, db_obj=teacher_obj, obj_in=teacher_in)
    return teacher_obj

@router.delete("/{teacher_id}")
def delete_teacher(
    *,
    db: Session = Depends(get_db),
    teacher_id: int,
):
    """
    Eliminar un profesor (marcar como inactivo).
    """
    teacher_obj = teacher.get(db, id=teacher_id)
    if not teacher_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profesor no encontrado"
        )
    
    # Marcar como inactivo en lugar de eliminar
    teacher_obj.is_active = False
    db.commit()
    return {"message": "Profesor eliminado exitosamente"} 