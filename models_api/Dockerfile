FROM python:3.10.12-slim
#install deps
RUN pip install "poetry==1.4.2"
COPY pyproject.toml ./
RUN poetry config installer.max-workers 4 && \
    poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction --no-ansi
WORKDIR /app
CMD ["uvicorn", "main:app",  "--workers", "2"]