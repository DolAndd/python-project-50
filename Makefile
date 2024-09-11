install:
	poetry install


prog:
	poetry run gendiff -h


build:
	poetry build


publish:
	poetry publish --dry-run


package-install:
	python3 -m pip install --user dist/*.whl


lint:
	poetry run flake8 brain_games


reinstall:
	python3 -m pip install  --force-reinstall dist/*.whl


update: install build publish reinstall


test-coverage:
	poetry run pytest --cov=brain_games --cov-report xml


test:
	poetry run pytest


selfcheck:
	poetry check


check: selfcheck test lint

