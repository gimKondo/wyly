# wyly-brain

Brain to predict "what is this?" for Wyly

## Requirement for Development

- Python 3.8.x
- [Poetry](https://github.com/python-poetry/poetry#installation)
  - package manager
- Linters and formatters
  - tools are installed by `poetry install`

## Setup Development Environment

### Setup virtual env and install dependency packages

- `poetry install`

### Update virtual env

- execute `poetry update` on adding/updating dependencies

### Run server

#### On Docker

1. build docker: `docker-compose build`
2. run docker: `docker-compose up -d`
3. test API: `curl http://127.0.0.1:8000`

#### On host OS

- `poetry run uvicorn app.main:app --reload`
