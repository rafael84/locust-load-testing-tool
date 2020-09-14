start-standard-local:
	@TARGET_HOST=http://awesome-web-app:3333 \
		LOCUSTFILE=standard.py \
		docker-compose up \
		--scale locust-worker=3 \
		--remove-orphans

start-standard-remote:
	@TARGET_HOST=https://awesome-web-app.vercel.app \
		LOCUSTFILE=standard.py \
		docker-compose up \
		--scale locust-worker=3 \
		--remove-orphans

start-browser-local:
	@TARGET_HOST=http://awesome-web-app:3333 \
		LOCUSTFILE=browser.py \
		docker-compose up \
		--scale locust-worker=3 \
		--remove-orphans

start-browser-remote:
	@TARGET_HOST=https://awesome-web-app.vercel.app \
		LOCUSTFILE=browser.py \
		docker-compose up \
		--scale locust-worker=3 \
		--remove-orphans

build:
	@docker-compose build

python:
	@docker run -it --rm \
		--entrypoint '/bin/bash' \
		--network locust-load-testing-tool_default \
		locust-load-testing-tool_locust-master:latest
