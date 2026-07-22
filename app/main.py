from fastapi import FastAPI

from app.core.database import Base, engine
from app.models.student import Student
from app.models.course import Course
from app.routers.students import router as student_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI Learning Journey",
    description="A practical project for learning professional backend development.",
    version="1.0.0",
)

app.include_router(student_router)


@app.get("/")
def read_root() -> dict[str, str]:
    return {
        "message": "FastAPI Learning Journey boshlandi!",
        "status": "success",
    }


@app.get("/health")
def health_check() -> dict[str, str]:
    return {
        "status": "healthy",
    }


@app.get("/about")
def read_about() -> dict[str, str]:
    return {
        "project": "FastAPI Learning Journey",
        "goal": "Senior Full Stack Developer bo'lish",
        "current_month": "Month 3",
        "current_lesson": "Lesson 1",
    }