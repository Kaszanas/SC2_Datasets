# Testing Commands

To run pytest with HTML coverage report executing minor tests:
```
poetry run pytest -m minor --ignore-glob='test_*.py' .\tests\test_cases\ --cov=sc2_datasets --cov-report term-missing --cov-report html --cov=xml
```

To run pytest with HTML coverage report executing all tests:
```
poetry run pytest --ignore-glob='test_*.py' .\tests\test_cases\ --cov=sc2_datasets --cov-report term-missing --cov-report html --cov=xml
```
