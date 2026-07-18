from sqlalchemy.orm import Session

from app.models.student import Student
from app.schemas.student import StudentCreate


class StudentRepository:

    def create(
        self,
        db: Session,
        student_data: StudentCreate,
    ):
        student = Student(
            name=student_data.name,
            age=student_data.age,
        )

        db.add(student)
        db.commit()
        db.refresh(student)

        return student