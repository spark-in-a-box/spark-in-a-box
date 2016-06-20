FROM {{ DOCKER_PREFIX }}/{{ DOCKER_NAME }}-base

ENTRYPOINT ["spark-submit"]
