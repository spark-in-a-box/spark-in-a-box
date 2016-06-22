FROM ubuntu:16.04

LABEL spark.version="{{ SPARK_VERSION }}" \
      hadoop.version="{{ HADOOP_FULL_VERSION }}" \
      scala.version="{{ SCALA_VERSION }}" \
      python.version="{{ PYTHON_VERSION }}" \
      python.hashseed="{{ PYTHON_HASHSEED }}"

ENV JAVA_HOME /usr/lib/jvm/java-{{ JDK_VERSION }}-openjdk-amd64

ENV CURL_CA_BUNDLE /etc/ssl/certs/ca-certificates.crt

ENV SPARK_HOME /home/{{ USERNAME }}/spark-{{ SPARK_VERSION }}

ENV PYSPARK_PYTHON /home/{{ USERNAME }}/anaconda{{ PYTHON_VERSION }}/bin/python
ENV PYTHON_HASHSEED {{ PYTHON_HASHSEED }}

# See https://github.com/phusion/baseimage-docker/issues/58
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

RUN apt-get update \
    && apt-get install -y wget \
    && apt-get install -y --no-install-recommends openjdk-{{ JDK_VERSION }}-jdk-headless \
    && apt-get install -y libatlas3-base libopenblas-base \
    && apt-get install -y bzip2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*ce

RUN groupadd -r {{ USERNAME }} && useradd -r -g {{ USERNAME }} {{ USERNAME }} \
    && mkdir /home/{{ USERNAME }} \
    && chown -R {{ USERNAME }}:{{ USERNAME }} /home/{{ USERNAME }}

USER {{ USERNAME }}

WORKDIR /home/{{ USERNAME }}

ENV PATH $PATH:/home/{{ USERNAME }}/anaconda{{ PYTHON_VERSION }}/bin

RUN wget {{ ANACONDA_URL }}/{{ ANACONDA_INSTALLER }} \
    && bash {{ ANACONDA_INSTALLER }} -b -p /home/{{ USERNAME }}/anaconda{{ PYTHON_VERSION }} \
    && rm {{ ANACONDA_INSTALLER }} \
    && conda install -y curl {{ PYTHON_PACKAGES }}

{% if WITH_R %}
RUN conda install -y -c r r
{% endif %}

{% if HADOOP_PROVIDED %}
RUN wget {{ HADOOP_DIST_URL }}/hadoop-{{ HADOOP_FULL_VERSION }}/hadoop-{{ HADOOP_FULL_VERSION }}.tar.gz -O - | tar -xz

ENV HADOOP_HOME /home/{{ USERNAME }}/hadoop-{{ HADOOP_FULL_VERSION }}
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:$HADOOP_HOME/lib/native
ENV PATH $PATH:$HADOOP_HOME/bin

RUN echo "export SPARK_DIST_CLASSPATH=$(hadoop classpath)" > .bashrc
{% endif %}

RUN wget {{ SPARK_DIST_URL }}/spark-{{ SPARK_VERSION }}/spark-{{ SPARK_VERSION }}.tgz -O - | tar -xz \
    && cd $SPARK_HOME \
    && dev/change-scala-version.sh {{ SCALA_VERSION }} \
    && build/mvn -Dscala-{{ SCALA_VERSION }} \
                 -Pnetlib-lgpl -DskipTests {{ MVN_PARAMS }} \
                 clean package

ENV PATH $PATH:$SPARK_HOME/bin
