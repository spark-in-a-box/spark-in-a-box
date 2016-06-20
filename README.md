A simple commandline utility to generate Docker images for testing and development of the Apache Spark applications.

## Installation 

```
pip install -e git://github.com/zero323/spark-in-a-box.git@v0.0.1#egg=sparkinabox
```

## Usage

```
usage: makebox [-h] [--username USERNAME]
               [--anaconda-repository ANACONDA_REPOSITORY]
               [--anaconda {anaconda,miniconda}] [--python {2,3}]
               [--python-packages [PYTHON_PACKAGES [PYTHON_PACKAGES ...]]]
               [--with-mkl] [--no-mkl] [--python-hashseed PYTHON_HASHSEED]
               [--scala {2.10,2.11}] [--spark {1.6.1,2.0.0-preview}]
               [--jdk {7,8}] [--hadoop-version HADOOP_VERSION]
               [--with-hadoop-provided] [--no-hadoop-provided] [--with-hive]
               [--no-hive] [--with-yarn] [--no-yarn] [--with-r] [--no-r]
               --output-dir OUTPUT_DIR

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
```
