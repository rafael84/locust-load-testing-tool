run:
	@docker-compose up \
		--scale locust-worker=3 \
		--remove-orphans

build:
	@docker-compose build

python:
	@docker run -it --rm \
		--entrypoint '/bin/bash' \
		--network locust-load-testing-tool_default \
		locust-load-testing-tool_locust-master:latest
