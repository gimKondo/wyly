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

- `poetry run uvicorn app.main:app --reload`
