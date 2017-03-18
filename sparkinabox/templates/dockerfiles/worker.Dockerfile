FROM {{ DOCKER_PREFIX }}/{{ DOCKER_NAME }}-base

CMD ["spark-class", "org.apache.spark.deploy.worker.Worker", "spark://master:7077"]
