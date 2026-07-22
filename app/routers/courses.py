from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.exceptions import course_not_found
from app.core.database import get_db
from app.schemas.course import (
    CourseCreate,
    CourseResponse,
)
from app.services.course_service import (
    create_course,
    get_all_courses,
    get_course_by_id,
)


router = APIRouter(
    prefix="/courses",
    tags=["Courses"],
)


@router.get(
    "/",
    response_model=list[CourseResponse],
)
def read_courses(
    db: Session = Depends(get_db),
):
    return get_all_courses(db=db)


@router.post(
    "/",
    response_model=CourseResponse,
    status_code=201,
)
def create_new_course(
    course_data: CourseCreate,
    db: Session = Depends(get_db),
):
    return create_course(
        db=db,
        course_data=course_data,
    )


@router.get(
    "/{course_id}",
    response_model=CourseResponse,
)
def read_course(
    course_id: int,
    db: Session = Depends(get_db),
):
    course = get_course_by_id(
        db=db,
        course_id=course_id,
    )

    if course is None:
        course_not_found()

    return course