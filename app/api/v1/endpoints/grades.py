from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.crud.grade import grade
from app.schemas.grade import GradeCreate, GradeUpdate, GradeResponse
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=GradeResponse, status_code=status.HTTP_201_CREATED)
def create_grade(
    *,
    db: Session = Depends(get_db),
    grade_in: GradeCreate,
):
    """
    Crear una nueva calificación.
    """
    # Validar que la calificación esté en el rango válido
    if grade_in.grade_value < 0 or grade_in.grade_value > grade_in.max_grade:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"La calificación debe estar entre 0 y {grade_in.max_grade}"
        )
    
    grade_obj = grade.create(db, obj_in=grade_in)
    return grade_obj

@router.get("/", response_model=List[GradeResponse])
def read_grades(
    db: Session = Depends(get_db),
    student_id: Optional[int] = None,
    class_id: Optional[int] = None,
    grade_type: Optional[str] = None,
):
    """
    Obtener lista de calificaciones.
    """
    if student_id and class_id:
        grades = grade.get_by_student_and_class(db, student_id=student_id, class_id=class_id)
    elif student_id:
        grades = grade.get_by_student(db, student_id=student_id)
    elif class_id:
        if grade_type:
            grades = grade.get_by_grade_type(db, class_id=class_id, grade_type=grade_type)
        else:
            grades = grade.get_by_class(db, class_id=class_id)
    else:
        grades = grade.get_multi(db)
    return grades

@router.get("/{grade_id}", response_model=GradeResponse)
def read_grade(
    *,
    db: Session = Depends(get_db),
    grade_id: int,
):
    """
    Obtener una calificación por ID.
    """
    grade_obj = grade.get(db, id=grade_id)
    if not grade_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Calificación no encontrada"
        )
    return grade_obj

@router.put("/{grade_id}", response_model=GradeResponse)
def update_grade(
    *,
    db: Session = Depends(get_db),
    grade_id: int,
    grade_in: GradeUpdate,
):
    """
    Actualizar una calificación.
    """
    grade_obj = grade.get(db, id=grade_id)
    if not grade_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Calificación no encontrada"
        )
    
    # Validar que la calificación esté en el rango válido
    if grade_in.grade_value is not None:
        max_grade = grade_in.max_grade or grade_obj.max_grade
        if grade_in.grade_value < 0 or grade_in.grade_value > max_grade:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"La calificación debe estar entre 0 y {max_grade}"
            )
    
    grade_obj = grade.update(db, db_obj=grade_obj, obj_in=grade_in)
    return grade_obj

@router.delete("/{grade_id}")
def delete_grade(
    *,
    db: Session = Depends(get_db),
    grade_id: int,
):
    """
    Eliminar una calificación.
    """
    grade_obj = grade.get(db, id=grade_id)
    if not grade_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Calificación no encontrada"
        )
    
    grade.remove(db, id=grade_id)
    return {"message": "Calificación eliminada exitosamente"}

@router.get("/student/{student_id}/class/{class_id}/average")
def get_student_average(
    *,
    db: Session = Depends(get_db),
    student_id: int,
    class_id: int,
):
    """
    Obtener el promedio de un estudiante en una clase específica.
    """
    average = grade.get_student_average(db, student_id=student_id, class_id=class_id)
    if average is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No se encontraron calificaciones para este estudiante en esta clase"
        )
    return {"student_id": student_id, "class_id": class_id, "average": average} 