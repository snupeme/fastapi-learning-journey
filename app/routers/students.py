from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

students = []


class Student(BaseModel):
    name: str
    age: int


@router.get("/students")
def get_students():
    return students


@router.post("/students")
def create_student(student: Student):
    students.append(student)

    return {
        "message": "Student created successfully",
        "student": student
    }


@router.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id < 0 or student_id >= len(students):
        raise HTTPException(
            status_code=404,
            detail="Student topilmadi"
        )

    return students[student_id]


@router.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id < 0 or student_id >= len(students):
        raise HTTPException(
            status_code=404,
            detail="Student topilmadi"
        )

    deleted_student = students.pop(student_id)

    return {
        "message": "Student muvaffaqiyatli o'chirildi",
        "student": deleted_student
    }