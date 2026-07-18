from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.student import (
    StudentCreate,
    StudentResponse,
    StudentUpdate,
)
from app.services import student_service


router = APIRouter(
    prefix="/students",
    tags=["Students"],
)


@router.post(
    "/",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db),
) -> StudentResponse:
    return student_service.create_student(
        db=db,
        student=student,
    )


@router.get(
    "/",
    response_model=list[StudentResponse],
)
def get_all_students(
    db: Session = Depends(get_db),
) -> list[StudentResponse]:
    return student_service.get_all_students(
        db=db,
    )


@router.get(
    "/{student_id}",
    response_model=StudentResponse,
)
def get_student_by_id(
    student_id: int,
    db: Session = Depends(get_db),
) -> StudentResponse:
    return student_service.get_student_by_id(
        db=db,
        student_id=student_id,
    )


@router.put(
    "/{student_id}",
    response_model=StudentResponse,
)
def update_student(
    student_id: int,
    student: StudentCreate,
    db: Session = Depends(get_db),
) -> StudentResponse:
    return student_service.update_student(
        db=db,
        student_id=student_id,
        student=student,
    )

@router.patch(
    "/{student_id}",
    response_model=StudentResponse,
)
def patch_student(
    student_id: int,
    student: StudentUpdate,
    db: Session = Depends(get_db),
) -> StudentResponse:
    return student_service.patch_student(
        db=db,
        student_id=student_id,
        student=student,
    )
@router.delete(
    "/{student_id}",
    response_model=StudentResponse,
)
def delete_student(
    student_id: int,
    db: Session = Depends(get_db),
) -> StudentResponse:
    return student_service.delete_student(
        db=db,
        student_id=student_id,
    )