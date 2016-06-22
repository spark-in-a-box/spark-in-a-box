build:
    docker build  -t {{ DOCKER_PREFIX }}/{{ DOCKER_NAME }}-base base
    docker-compose build

up: build
    docker-compose up -d

down:
    docker-compose down --rmi all