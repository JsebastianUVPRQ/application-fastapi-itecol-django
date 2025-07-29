from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.crud.class_crud import class_crud, class_enrollment
from app.schemas.class_schema import ClassCreate, ClassUpdate, ClassResponse, ClassEnrollmentCreate, ClassEnrollmentResponse
from app.db.session import get_db

router = APIRouter()

# Endpoints para Clases
@router.post("/", response_model=ClassResponse, status_code=status.HTTP_201_CREATED)
def create_class(
    *,
    db: Session = Depends(get_db),
    class_in: ClassCreate,
):
    """
    Crear una nueva clase.
    """
    class_obj = class_crud.create(db, obj_in=class_in)
    return class_obj

@router.get("/", response_model=List[ClassResponse])
def read_classes(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    teacher_id: Optional[int] = None,
    subject_id: Optional[int] = None,
    grade_level: Optional[int] = None,
):
    """
    Obtener lista de clases.
    """
    if teacher_id:
        classes = class_crud.get_by_teacher(db, teacher_id=teacher_id)
    elif subject_id:
        classes = class_crud.get_by_subject(db, subject_id=subject_id)
    elif grade_level:
        classes = class_crud.get_by_grade_level(db, grade_level=grade_level)
    else:
        classes = class_crud.get_active_classes(db, skip=skip, limit=limit)
    return classes

@router.get("/{class_id}", response_model=ClassResponse)
def read_class(
    *,
    db: Session = Depends(get_db),
    class_id: int,
):
    """
    Obtener una clase por ID.
    """
    class_obj = class_crud.get(db, id=class_id)
    if not class_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Clase no encontrada"
        )
    return class_obj

@router.put("/{class_id}", response_model=ClassResponse)
def update_class(
    *,
    db: Session = Depends(get_db),
    class_id: int,
    class_in: ClassUpdate,
):
    """
    Actualizar una clase.
    """
    class_obj = class_crud.get(db, id=class_id)
    if not class_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Clase no encontrada"
        )
    
    class_obj = class_crud.update(db, db_obj=class_obj, obj_in=class_in)
    return class_obj

@router.delete("/{class_id}")
def delete_class(
    *,
    db: Session = Depends(get_db),
    class_id: int,
):
    """
    Eliminar una clase (marcar como inactiva).
    """
    class_obj = class_crud.get(db, id=class_id)
    if not class_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Clase no encontrada"
        )
    
    # Marcar como inactiva en lugar de eliminar
    class_obj.is_active = False
    db.commit()
    return {"message": "Clase eliminada exitosamente"}

# Endpoints para Matrículas
@router.post("/enrollments/", response_model=ClassEnrollmentResponse, status_code=status.HTTP_201_CREATED)
def create_enrollment(
    *,
    db: Session = Depends(get_db),
    enrollment_in: ClassEnrollmentCreate,
):
    """
    Matricular un estudiante en una clase.
    """
    # Verificar si ya está matriculado
    existing_enrollment = class_enrollment.get_enrollment(
        db, student_id=enrollment_in.student_id, class_id=enrollment_in.class_id
    )
    if existing_enrollment:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El estudiante ya está matriculado en esta clase"
        )
    
    enrollment_obj = class_enrollment.create(db, obj_in=enrollment_in)
    return enrollment_obj

@router.get("/enrollments/", response_model=List[ClassEnrollmentResponse])
def read_enrollments(
    db: Session = Depends(get_db),
    student_id: Optional[int] = None,
    class_id: Optional[int] = None,
):
    """
    Obtener lista de matrículas.
    """
    if student_id:
        enrollments = class_enrollment.get_by_student(db, student_id=student_id)
    elif class_id:
        enrollments = class_enrollment.get_by_class(db, class_id=class_id)
    else:
        enrollments = class_enrollment.get_multi(db)
    return enrollments

@router.delete("/enrollments/{enrollment_id}")
def delete_enrollment(
    *,
    db: Session = Depends(get_db),
    enrollment_id: int,
):
    """
    Cancelar matrícula (marcar como inactiva).
    """
    enrollment_obj = class_enrollment.get(db, id=enrollment_id)
    if not enrollment_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Matrícula no encontrada"
        )
    
    # Marcar como inactiva en lugar de eliminar
    enrollment_obj.is_active = False
    db.commit()
    return {"message": "Matrícula cancelada exitosamente"} 