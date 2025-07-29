from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.crud.subject import subject
from app.schemas.subject import SubjectCreate, SubjectUpdate, SubjectResponse
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=SubjectResponse, status_code=status.HTTP_201_CREATED)
def create_subject(
    *,
    db: Session = Depends(get_db),
    subject_in: SubjectCreate,
):
    """
    Crear una nueva asignatura.
    """
    # Verificar si el código ya existe
    existing_subject = subject.get_by_code(db, code=subject_in.code)
    if existing_subject:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ya existe una asignatura con este código"
        )
    
    subject_obj = subject.create(db, obj_in=subject_in)
    return subject_obj

@router.get("/", response_model=List[SubjectResponse])
def read_subjects(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    grade_level: Optional[int] = None,
):
    """
    Obtener lista de asignaturas.
    """
    if grade_level:
        subjects = subject.get_by_grade_level(db, grade_level=grade_level)
    else:
        subjects = subject.get_active_subjects(db, skip=skip, limit=limit)
    return subjects

@router.get("/{subject_id}", response_model=SubjectResponse)
def read_subject(
    *,
    db: Session = Depends(get_db),
    subject_id: int,
):
    """
    Obtener una asignatura por ID.
    """
    subject_obj = subject.get(db, id=subject_id)
    if not subject_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Asignatura no encontrada"
        )
    return subject_obj

@router.put("/{subject_id}", response_model=SubjectResponse)
def update_subject(
    *,
    db: Session = Depends(get_db),
    subject_id: int,
    subject_in: SubjectUpdate,
):
    """
    Actualizar una asignatura.
    """
    subject_obj = subject.get(db, id=subject_id)
    if not subject_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Asignatura no encontrada"
        )
    
    # Verificar si el nuevo código ya existe
    if subject_in.code and subject_in.code != subject_obj.code:
        existing_subject = subject.get_by_code(db, code=subject_in.code)
        if existing_subject:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ya existe una asignatura con este código"
            )
    
    subject_obj = subject.update(db, db_obj=subject_obj, obj_in=subject_in)
    return subject_obj

@router.delete("/{subject_id}")
def delete_subject(
    *,
    db: Session = Depends(get_db),
    subject_id: int,
):
    """
    Eliminar una asignatura (marcar como inactiva).
    """
    subject_obj = subject.get(db, id=subject_id)
    if not subject_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Asignatura no encontrada"
        )
    
    # Marcar como inactiva en lugar de eliminar
    subject_obj.is_active = False
    db.commit()
    return {"message": "Asignatura eliminada exitosamente"} 