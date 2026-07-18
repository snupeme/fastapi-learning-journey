from pydantic import BaseModel, ConfigDict, Field


class StudentCreate(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=50,
    )

    age: int = Field(
        ge=5,
        le=100,
    )


class StudentUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=2,
        max_length=50,
    )

    age: int | None = Field(
        default=None,
        ge=5,
        le=100,
    )


class StudentResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int
    name: str
    age: int