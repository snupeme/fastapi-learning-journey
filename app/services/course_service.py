from sqlalchemy.orm import Session

from app.models.course import Course
from app.repositories.course_repository import CourseRepository
from app.schemas.course import (
    CourseCreate,
    CourseUpdate,
)


course_repository = CourseRepository()


def create_course(
    db: Session,
    course_data: CourseCreate,
) -> Course:
    return course_repository.create(
        db=db,
        course_data=course_data,
    )


def get_all_courses(
    db: Session,
) -> list[Course]:
    return course_repository.get_all(
        db=db,
    )


def get_course_by_id(
    db: Session,
    course_id: int,
) -> Course | None:
    return course_repository.get_by_id(
        db=db,
        course_id=course_id,
    )