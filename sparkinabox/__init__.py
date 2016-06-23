#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function)
import random
import argparse

from sparkinabox.release import __author__, __version__
from sparkinabox.makebox import make_box


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--username", default="spark", help="User name which will be used in the containers.")

    parser.add_argument("--anaconda-repository", default="https://repo.continuum.io/",
                        help="URL which should be used to download Anaconda installers.")
    parser.add_argument("--anaconda", choices=["anaconda", "miniconda"], default="miniconda",
                        help="Anaconda version to be installed on all nodes.")

    parser.add_argument("--python", choices=["2", "3"], default="3")
    parser.add_argument("--python-packages", nargs="*",
                        default="numpy scipy scikit-learn numexpr numba curl toolz dask",
                        help="A list of Python packages to be installed on all nodes."
                        )

    mkl_parser = parser.add_mutually_exclusive_group(required=False)
    mkl_parser.add_argument('--with-mkl', dest='nomkl', action="store_false",
                            help="Use Python packages (NumpPy, SciPy) build using MKL")
    mkl_parser.add_argument('--no-mkl', dest='nomkl', action="store_true",
                            help="Use Python packages using LGPL libraries.")
    mkl_parser.set_defaults(nomkl=True)

    parser.add_argument("--python-hashseed", default=random.randint(0, 2 ** 31 - 1), type=int,
                        help="HASHSEED for Python interpreters. Random by default.")

    parser.add_argument("--scala", choices=["2.10", "2.11"], default="2.11",
                        help="Scala version which should be used to compile Spark.")
    parser.add_argument("--spark", choices=["1.6.1", "2.0.0-preview"], default="2.0.0-preview",
                        help="Version of Spark which should be compiled.")
    parser.add_argument("--jdk", choices=["7", "8"], default="8",
                        help="JDK version."),

    parser.add_argument("--hadoop-version", default="2.7.2",
                        help="Hadoop version to be used.")

    hadoop_provided_parser = parser.add_mutually_exclusive_group(required=False)
    hadoop_provided_parser.add_argument("--with-hadoop-provided", dest="with_hadoop_provided", action="store_true",
                                        help="Download standalone Hadoop libraries.")
    hadoop_provided_parser.add_argument("--no-hadoop-provided", dest="with_hadoop_provided", action="store_false",
                                        help="Build Spark with embedded Hadoop.")
    hadoop_provided_parser.set_defaults(hadoop_provided=True)

    hive_parser = parser.add_mutually_exclusive_group(required=False)
    hive_parser.add_argument("--with-hive", dest="with_hive", action="store_true",
                             help="Build Spark with Hive support.")
    hive_parser.add_argument("--no-hive", dest="with_hive", action="store_false",
                             help="Build Spark without Hive support.")

    hive_parser.set_defaults(with_hive=True)

    yarn_parser = parser.add_mutually_exclusive_group(required=False)
    yarn_parser.add_argument("--with-yarn", dest="with_yarn", action="store_true",
                             help="Build Spark with Yarn.")
    yarn_parser.add_argument("--no-yarn", dest="with_yarn", action="store_false",
                             help="Build Spark without Yarn.")
    yarn_parser.set_defaults(wiht_yarn=False)

    r_parser = parser.add_mutually_exclusive_group(required=False)
    r_parser.add_argument("--with-r", dest="with_r", action="store_true",
                          help="Install R and build Spark with SparkR")
    r_parser.add_argument("--no-r", dest="with_r", action="store_false",
                          help="Don't install R.")
    r_parser.set_defaults(with_r=False)

    parser.add_argument("--output-dir", dest="output_dir", required=True,
                        help="Output directory to put Dockerfiles.")

    parser.add_argument("--docker-prefix", dest="docker_prefix", default="zero323",
                        help="Image will be named {docker-prefix}/{docker-name}-{role}.")
    parser.add_argument("--docker-name", dest="docker_name", default="spark-sandbox")

    parser.add_argument("--profile", choices=["local", "standalone"], default="local")
    parser.add_argument("--client-entrypoint",
                        choices=["spark-submit", "spark-shell", "pyspark", "sparkR"],
                        default="spark-submit",
                        help="Entry point to be used by the client image.")

    make_box(parser.parse_args())
