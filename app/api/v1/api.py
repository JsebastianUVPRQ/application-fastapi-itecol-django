from fastapi import APIRouter
from app.api.v1.endpoints import students, teachers, subjects, classes, grades, logs

api_router = APIRouter()

api_router.include_router(students.router, prefix="/students", tags=["students"])
api_router.include_router(teachers.router, prefix="/teachers", tags=["teachers"])
api_router.include_router(subjects.router, prefix="/subjects", tags=["subjects"])
api_router.include_router(classes.router, prefix="/classes", tags=["classes"])
api_router.include_router(grades.router, prefix="/grades", tags=["grades"])
api_router.include_router(logs.router, prefix="/logs", tags=["logs"]) 