from fastapi import APIRouter, HTTPException

from app.schemas.student import Student


router = APIRouter(
    prefix="/students",
    tags=["Students"],
)

students = []


@router.get("/", response_model=list[Student])
def get_students():
    return students


@router.post("/")
def create_student(student: Student):
    students.append(student)

    return {
        "message": "Student created successfully",
        "student": student,
    }


@router.get("/{student_id}", response_model=Student)
def get_student(student_id: int):
    if student_id < 0 or student_id >= len(students):
        raise HTTPException(
            status_code=404,
            detail="Student topilmadi",
        )

    return students[student_id]


@router.delete("/{student_id}")
def delete_student(student_id: int):
    if student_id < 0 or student_id >= len(students):
        raise HTTPException(
            status_code=404,
            detail="Student topilmadi",
        )

    deleted_student = students.pop(student_id)

    return {
        "message": "Student muvaffaqiyatli o'chirildi",
        "student": deleted_student,
    }