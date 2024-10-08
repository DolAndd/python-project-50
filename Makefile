install:
	poetry install


prog:
	poetry run gendiff


build:
	poetry build


publish:
	poetry publish --dry-run


package-install:
	python3 -m pip install --user dist/*.whl


lint:
	poetry run flake8 gendiff


reinstall:
	python3 -m pip install  --force-reinstall dist/*.whl


update: install build publish reinstall


test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml


test:
	poetry run pytest


selfcheck:
	poetry check


check: test lint

