install:
	poetry install

lint:
	poetry run flake8 src

coverage:
	poetry run pytest --cov=src --cov-report xml tests/

test:
	poetry run pytest
