import math
import random
from fastapi import HTTPException

from src.config.settings import COLORS
from .schemas import SquareEquationResponse, RandomChoiceResponse


async def quadratic_equation_solution(a: float, b: float, c: float) -> SquareEquationResponse:
    """
    Calculate the solution of a quadratic equation.
    :param a: coefficient of x^2
    :param b: coefficient of x
    :param c: constant
    :return: list of solutions
    """
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        raise HTTPException(status_code=400, detail="delta is negative")
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    return SquareEquationResponse(solutions={x1, x2})


async def random_choice(number: int) -> RandomChoiceResponse:
    """
    Return a random color.
    :param number: number of color to return
    :return: random color
    """
    colors = []
    for color, count in COLORS.items():
        colors.extend([color] * count)
    random.shuffle(colors)

    return RandomChoiceResponse(color=colors[number - 1])
