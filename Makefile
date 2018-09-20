init:
	pip install pipenv
	pipenv install --dev

test:
	pipenv run pytest --cov=betbright --flake8 tests
