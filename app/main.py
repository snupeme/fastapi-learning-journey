from fastapi import FastAPI

from app.routers.students import router as student_router


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
        "current_month": "Month 1",
        "current_lesson": "Lesson 10",
    }


@app.get("/contact")
def read_contact() -> dict[str, str]:
    return {
        "email": "example@example.com",
        "github": "GitHub profilingiz",
    }


@app.get("/hello/{name}")
def say_hello(name: str):
    return {
        "message": f"Hello, {name}!"
    }


@app.get("/square/{number}")
def square(number: int):
    return {
        "number": number,
        "square": number * number,
    }