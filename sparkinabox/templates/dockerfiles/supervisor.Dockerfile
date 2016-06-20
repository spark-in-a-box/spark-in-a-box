FROM {{ DOCKER_PREFIX }}/{{ DOCKER_NAME }}-base

ENTRYPOINT ["spark-class"]

CMD ["org.apache.spark.deploy.master.Master"]
