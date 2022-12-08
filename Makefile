install:
	poetry install 

dev:
	poetry run flask --app rest_api:app run