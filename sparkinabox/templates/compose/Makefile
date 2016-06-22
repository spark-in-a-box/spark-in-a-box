build: build_base
	docker-compose build

build_base:
	docker build  -t {{ DOCKER_PREFIX }}/{{ DOCKER_NAME }}-base base

up: build
	docker-compose up -d

down:
	docker-compose down

