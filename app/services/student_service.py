from sqlalchemy.orm import Session

from app.core.exceptions import student_not_found
from app.models.student import Student
from app.repositories.student_repository import StudentRepository
from app.schemas.student import StudentCreate, StudentUpdate


student_repository = StudentRepository()


def create_student(
    db: Session,
    student: StudentCreate,
) -> Student:
    return student_repository.create(
        db=db,
        student_data=student,
    )


def get_all_students(
    db: Session,
) -> list[Student]:
    return student_repository.get_all(
        db=db,
    )


def get_student_by_id(
    db: Session,
    student_id: int,
) -> Student:
    student = student_repository.get_by_id(
        db=db,
        student_id=student_id,
    )

    if student is None:
        student_not_found()

    return student


def update_student(
    db: Session,
    student_id: int,
    student: StudentCreate,
) -> Student:
    updated_student = student_repository.update(
        db=db,
        student_id=student_id,
        student_data=student,
    )

    if updated_student is None:
        student_not_found()

    return updated_student

def patch_student(
    db: Session,
    student_id: int,
    student: StudentUpdate,
) -> Student:
    updated_student = student_repository.patch(
        db=db,
        student_id=student_id,
        student_data=student,
    )

    if updated_student is None:
        student_not_found()

    return updated_student

def delete_student(
    db: Session,
    student_id: int,
) -> Student:
    deleted_student = student_repository.delete(
        db=db,
        student_id=student_id,
    )

    if deleted_student is None:
        student_not_found()

    return deleted_student