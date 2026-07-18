from typing import NoReturn

from fastapi import HTTPException, status


def student_not_found() -> NoReturn:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Student topilmadi",
    )