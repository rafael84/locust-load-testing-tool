run:
	@docker-compose up --scale worker=3

build:
	@docker-compose build
