FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-2021-10-02

WORKDIR /app

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

RUN apt-get -y update
RUN apt-get -y upgrade

COPY ./pyproject.toml ./poetry.lock* /app/

RUN poetry install

COPY . .
