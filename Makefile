format:
	ruff check --fix ml_service
	ruff format ml_service

lint:
	ruff check ml_service
	ruff format --check ml_service

tests:
	pytest test
