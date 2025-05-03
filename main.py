from fastapi import FastAPI
from core.config import settings
from api.v1.endpoints import auth, users, classrooms, grades
from dependencies.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="School Management System")

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(classrooms.router, prefix="/classrooms", tags=["Classrooms"])
app.include_router(grades.router, prefix="/grades", tags=["Grades"])

@app.get("/health-check")
def health_check():
    return {"status": "ok"}