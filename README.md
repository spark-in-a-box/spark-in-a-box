A simple commandline utility to generate Docker images for testing and development of the Apache Spark applications.

## Installation 

```
pip install -e git://github.com/zero323/spark-in-a-box.git@v0.0.8#egg=sparkinabox
```

## Usage

### Arguments

```
usage: makebox [-h] [--username USERNAME]
               [--anaconda-repository ANACONDA_REPOSITORY]
               [--anaconda {anaconda,miniconda}] [--python {2,3}]
               [--python-packages [PYTHON_PACKAGES [PYTHON_PACKAGES ...]]]
               [--with-mkl | --no-mkl] [--python-hashseed PYTHON_HASHSEED]
               [--scala {2.10,2.11}]
               [--spark {1.6.1,1.6.2,1.6.3,2.0.0,2.0.1,2.0.2}] [--jdk {7,8}]
               [--hadoop-version HADOOP_VERSION]
               [--with-hadoop-provided | --no-hadoop-provided]
               [--with-hive | --no-hive] [--with-yarn | --no-yarn]
               [--with-r | --no-r] --output-dir OUTPUT_DIR
               [--docker-prefix DOCKER_PREFIX] [--docker-name DOCKER_NAME]
               [--profile {local,standalone}]
               [--client-entrypoint {spark-submit,spark-shell,pyspark,sparkR}]
               [--mvn-artifacts [MVN_ARTIFACTS [MVN_ARTIFACTS ...]]]

optional arguments:
  -h, --help            show this help message and exit
  --username USERNAME   User name which will be used in the containers.
  --anaconda-repository ANACONDA_REPOSITORY
                        URL which should be used to download Anaconda
                        installers.
  --anaconda {anaconda,miniconda}
                        Anaconda version to be installed on all nodes.
  --python {2,3}
  --python-packages [PYTHON_PACKAGES [PYTHON_PACKAGES ...]]
                        A list of Python packages to be installed on all
                        nodes.
  --with-mkl            Use Python packages (NumpPy, SciPy) build using MKL
  --no-mkl              Use Python packages using LGPL libraries.
  --python-hashseed PYTHON_HASHSEED
                        Hash seed for Python interpreters. Random by
                        default.See:
                        http://stackoverflow.com/q/36798833/1560062
  --scala {2.10,2.11}   Scala version which should be used to compile Spark.
  --spark {1.6.1,1.6.2,1.6.3,2.0.0,2.0.1,2.0.2}
                        Version of Spark which should be compiled.
  --jdk {7,8}           JDK version.
  --hadoop-version HADOOP_VERSION
                        Hadoop version to be used.
  --with-hadoop-provided
                        Download standalone Hadoop libraries.
  --no-hadoop-provided  Build Spark with embedded Hadoop.
  --with-hive           Build Spark with Hive support.
  --no-hive             Build Spark without Hive support.
  --with-yarn           Build Spark with Yarn.
  --no-yarn             Build Spark without Yarn.
  --with-r              Install R and build Spark with SparkR
  --no-r                Don't install R.
  --output-dir OUTPUT_DIR
                        Output directory to put Dockerfiles.
  --docker-prefix DOCKER_PREFIX
                        Image will be named {docker-prefix}/{docker-
                        name}-{role}.
  --docker-name DOCKER_NAME
  --profile {local,standalone}
  --client-entrypoint {spark-submit,spark-shell,pyspark,sparkR}
                        Entry point to be used by the client image.
  --mvn-artifacts [MVN_ARTIFACTS [MVN_ARTIFACTS ...]]
                        A list of Maven artifacts which should be available on
                        each machine (space separated list in format
                        groupId:artifactId:version)
```

### Example session

```bash
# Create docker files
makebox --python-hashseed 323 --output-dir sparkinabox --profile standalone --spark 2.0.0-preview 
cd sparkinabox
# Build images
make build
# Start cluster
make up
# Add worker
docker-compose scale worker=2
# Submit PI example 
docker-compose run client --master spark://master:7077 \
               "/home/spark/spark-2.0.0-preview/examples/src/main/python/pi.py" 10
# Stop cluster
make down
```
 
