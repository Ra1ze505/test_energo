from pydantic import BaseModel, validator


class SquareEquation(BaseModel):
    a: float
    b: float = 0.0
    c: float = 0.0

    @validator('a')
    def validate_a(cls, v):
        if v == 0:
            raise ValueError('a cannot be zero')
        return v


class SquareEquationResponse(BaseModel):
    solutions: list[float]


class RandomChoice(BaseModel):
    number: int

    @validator('number')
    def validate_number(cls, v):
        if v <= 0:
            raise ValueError('number cannot be negative')
        elif v > 100:
            raise ValueError('number cannot be greater than 100')
        return v


class RandomChoiceResponse(BaseModel):
    color: str
