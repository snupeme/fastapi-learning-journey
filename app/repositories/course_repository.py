from sqlalchemy.orm import Session

from app.models.course import Course
from app.schemas.course import CourseCreate


class CourseRepository:
    def create(
        self,
        db: Session,
        course_data: CourseCreate,
    ) -> Course:
        course = Course(
            name=course_data.name,
        )

        db.add(course)
        db.commit()
        db.refresh(course)

        return course

    def get_all(
        self,
        db: Session,
    ) -> list[Course]:
        return db.query(Course).all()

    def get_by_id(
        self,
        db: Session,
        course_id: int,
    ) -> Course | None:
        return (
            db.query(Course)
            .filter(Course.id == course_id)
            .first()
        )