FROM {{ DOCKER_PREFIX }}/{{ DOCKER_NAME }}-base

ENTRYPOINT ["{{ CLIENT_ENTRYPOINT }}"]

{% if CLIENT_ENTRYPOINT == "spark-submit" %}
CMD ["--version", "."]
{% endif %}