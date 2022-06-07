from fastapi import APIRouter

from . import services, schemas

utils = APIRouter()


@utils.post('/quadratic_equation', response_model=schemas.SquareEquationResponse)
async def execute_sql(arguments: schemas.SquareEquation):
    return await services.quadratic_equation_solution(**arguments.dict())


@utils.post('/random_choice', response_model=schemas.RandomChoiceResponse)
async def random_choice(arguments: schemas.RandomChoice):
    return await services.random_choice(**arguments.dict())
