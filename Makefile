init:
	pip install pipenv
	pipenv install --dev

test:
	pipenv run pytest --cov=betbright --cov-report term-missing --flake8 tests
