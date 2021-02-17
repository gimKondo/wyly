# Container to export requiremnts.txt by poetry
# (beause of separating poetry from runtime container)
FROM python:3.8-slim as poetry-exporter
WORKDIR /app
RUN pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry export --without-hashes -f requirements.txt > requirements.txt

# Runtime container
FROM python:3.8-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY --from=poetry-exporter /app/requirements.txt .
RUN pip install -r requirements.txt
COPY ./app .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080" ]
