#!/usr/bin/env python3
"""
Script para inicializar la base de datos con datos de ejemplo.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.student import Student
from app.models.teacher import Teacher
from app.models.subject import Subject
from app.models.class_model import Class
from datetime import date, datetime

def init_db():
    """Inicializar la base de datos con datos de ejemplo."""
    db = SessionLocal()
    try:
        # Crear estudiantes de ejemplo
        students = [
            Student(
                student_id="EST001",
                first_name="Juan",
                last_name="Pérez",
                email="juan.perez@email.com",
                phone="123456789",
                date_of_birth=date(2015, 3, 15),
                address="Calle Principal 123",
                grade_level=3,
                is_active=True
            ),
            Student(
                student_id="EST002",
                first_name="María",
                last_name="García",
                email="maria.garcia@email.com",
                phone="987654321",
                date_of_birth=date(2014, 7, 22),
                address="Avenida Central 456",
                grade_level=4,
                is_active=True
            ),
            Student(
                student_id="EST003",
                first_name="Carlos",
                last_name="López",
                email="carlos.lopez@email.com",
                phone="555123456",
                date_of_birth=date(2016, 1, 10),
                address="Plaza Mayor 789",
                grade_level=2,
                is_active=True
            )
        ]
        
        for student in students:
            db.add(student)
        
        # Crear profesores de ejemplo
        teachers = [
            Teacher(
                teacher_id="PROF001",
                first_name="Ana",
                last_name="Rodríguez",
                email="ana.rodriguez@escuela.com",
                phone="111222333",
                date_of_birth=date(1985, 5, 12),
                address="Calle de los Maestros 1",
                specialization="Matemáticas",
                is_active=True
            ),
            Teacher(
                teacher_id="PROF002",
                first_name="Luis",
                last_name="Martínez",
                email="luis.martinez@escuela.com",
                phone="444555666",
                date_of_birth=date(1980, 9, 8),
                address="Avenida de la Educación 2",
                specialization="Lenguaje",
                is_active=True
            ),
            Teacher(
                teacher_id="PROF003",
                first_name="Carmen",
                last_name="Fernández",
                email="carmen.fernandez@escuela.com",
                phone="777888999",
                date_of_birth=date(1988, 12, 3),
                address="Plaza de la Ciencia 3",
                specialization="Ciencias",
                is_active=True
            )
        ]
        
        for teacher in teachers:
            db.add(teacher)
        
        # Crear asignaturas de ejemplo
        subjects = [
            Subject(
                name="Matemáticas",
                code="MAT001",
                description="Matemáticas básicas para primaria",
                grade_level=3,
                is_active=True
            ),
            Subject(
                name="Lenguaje",
                code="LEN001",
                description="Lenguaje y comunicación",
                grade_level=4,
                is_active=True
            ),
            Subject(
                name="Ciencias",
                code="CIE001",
                description="Ciencias naturales",
                grade_level=2,
                is_active=True
            ),
            Subject(
                name="Historia",
                code="HIS001",
                description="Historia y geografía",
                grade_level=3,
                is_active=True
            )
        ]
        
        for subject in subjects:
            db.add(subject)
        
        # Crear clases de ejemplo
        classes = [
            Class(
                name="Matemáticas 3° A",
                subject_id=1,
                teacher_id=1,
                grade_level=3,
                schedule="Lunes y Miércoles 8:00-9:30",
                room="Aula 101",
                max_students=25,
                is_active=True
            ),
            Class(
                name="Lenguaje 4° B",
                subject_id=2,
                teacher_id=2,
                grade_level=4,
                schedule="Martes y Jueves 9:30-11:00",
                room="Aula 102",
                max_students=25,
                is_active=True
            ),
            Class(
                name="Ciencias 2° C",
                subject_id=3,
                teacher_id=3,
                grade_level=2,
                schedule="Viernes 10:00-11:30",
                room="Laboratorio 1",
                max_students=20,
                is_active=True
            )
        ]
        
        for class_obj in classes:
            db.add(class_obj)
        
        db.commit()
        print("✅ Base de datos inicializada exitosamente con datos de ejemplo.")
        
    except Exception as e:
        db.rollback()
        print(f"❌ Error al inicializar la base de datos: {e}")
        raise
    finally:
        db.close()

if __name__ == "__main__":
    print("🚀 Inicializando base de datos...")
    init_db()
    print("✅ ¡Listo!") 