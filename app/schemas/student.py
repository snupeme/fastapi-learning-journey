from pydantic import BaseModel, Field


class Student(BaseModel):
    name: str = Field(
        min_length=3,
        max_length=50
    )

    age: int = Field(
        ge=16,
        le=100
    )