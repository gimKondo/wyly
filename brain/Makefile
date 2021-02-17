# -------------------
# set variables
# -------------------


# -------------------
# Test & Lint
# -------------------
test:
	GOOGLE_APPLICATION_CREDENTIALS=./app/credential/gcp-sa-key.json poetry run pytest

lint:
	poetry run black . --check
	poetry run isort . --check
	poetry run mypy .
	poetry run flake8 .

check:
	make test
	make lint

# -------------------
# API server
# -------------------
build:
	docker-compose build

run:
	docker-compose up -d

stop:
	docker-compose stop

ping:
	curl http://127.0.0.1:8000

log:
	docker-compose logs -f
