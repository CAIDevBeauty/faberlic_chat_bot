FROM python:3.10.12-slim

RUN pip install "poetry==1.4.2"
COPY pyproject.toml ./
RUN poetry config installer.max-workers 4 && \
    poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction --no-ansi

COPY . /app
WORKDIR app
CMD ["python3", "main.py" ]
