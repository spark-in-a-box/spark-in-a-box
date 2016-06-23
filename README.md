A simple commandline utility to generate Docker images for testing and development of the Apache Spark applications.

## Installation 

```
pip install -e git://github.com/zero323/spark-in-a-box.git@v0.0.6#egg=sparkinabox
```

## Usage

### Arguments

```
usage: makebox [-h] [--username USERNAME]
               [--anaconda-repository ANACONDA_REPOSITORY]
               [--anaconda {anaconda,miniconda}] [--python {2,3}]
               [--python-packages [PYTHON_PACKAGES [PYTHON_PACKAGES ...]]]
               [--with-mkl | --no-mkl] [--python-hashseed PYTHON_HASHSEED]
               [--scala {2.10,2.11}] [--spark {1.6.1,2.0.0-preview}]
               [--jdk {7,8}] [--hadoop-version HADOOP_VERSION]
               [--with-hadoop-provided | --no-hadoop-provided]
               [--with-hive | --no-hive] [--with-yarn | --no-yarn]
               [--with-r | --no-r] --output-dir OUTPUT_DIR
               [--docker-prefix DOCKER_PREFIX] [--docker-name DOCKER_NAME]
               [--profile {local,standalone}]
               [--client-entrypoint {spark-submit,spark-shell,pyspark,sparkR}]

optional arguments:
  -h, --help            show this help message and exit
  --username USERNAME
  --anaconda-repository ANACONDA_REPOSITORY
  --anaconda {anaconda,miniconda}
  --python {2,3}
  --python-packages [PYTHON_PACKAGES [PYTHON_PACKAGES ...]]
  --with-mkl
  --no-mkl
  --python-hashseed PYTHON_HASHSEED
  --scala {2.10,2.11}
  --spark {1.6.1,2.0.0-preview}
  --jdk {7,8}
  --hadoop-version HADOOP_VERSION
  --with-hadoop-provided
  --no-hadoop-provided
  --with-hive
  --no-hive
  --with-yarn
  --no-yarn
  --with-r
  --no-r
  --output-dir OUTPUT_DIR
  --docker-prefix DOCKER_PREFIX
  --docker-name DOCKER_NAME
  --profile {local,standalone}
  --client-entrypoint {spark-submit,spark-shell,pyspark,sparkR}
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
 
