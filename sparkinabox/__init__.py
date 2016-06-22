#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function)
import random
import argparse

from sparkinabox.release import __author__, __version__
from sparkinabox.makebox import make_box


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--username", default="spark")

    parser.add_argument("--anaconda-repository", default="https://repo.continuum.io/")
    parser.add_argument("--anaconda", choices=["anaconda", "miniconda"], default="miniconda")

    parser.add_argument("--python", choices=["2", "3"], default="3")
    parser.add_argument("--python-packages", nargs="*",
                        default="numpy scipy scikit-learn numexpr numba curl toolz dask")

    mkl_parser = parser.add_mutually_exclusive_group(required=False)
    mkl_parser.add_argument('--with-mkl', dest='nomkl', action="store_false")
    mkl_parser.add_argument('--no-mkl', dest='nomkl', action="store_true")
    mkl_parser.set_defaults(nomkl=True)

    parser.add_argument("--python-hashseed", default=random.randint(0, 2 ** 31 - 1), type=int)

    parser.add_argument("--scala", choices=["2.10", "2.11"], default="2.11")
    parser.add_argument("--spark", choices=["1.6.1", "2.0.0-preview"], default="2.0.0-preview")
    parser.add_argument("--jdk", choices=["7", "8"], default="8"),

    parser.add_argument("--hadoop-version", default="2.7.2")

    hadoop_provided_parser = parser.add_mutually_exclusive_group(required=False)
    hadoop_provided_parser.add_argument("--with-hadoop-provided", dest="with_hadoop_provided", action="store_true")
    hadoop_provided_parser.add_argument("--no-hadoop-provided", dest="with_hadoop_provided", action="store_false")
    hadoop_provided_parser.set_defaults(hadoop_provided=True)

    hive_parser = parser.add_mutually_exclusive_group(required=False)
    hive_parser.add_argument("--with-hive", dest="with_hive", action="store_true")
    hive_parser.add_argument("--no-hive", dest="with_hive", action="store_false")
    hive_parser.set_defaults(with_hive=True)

    yarn_parser = parser.add_mutually_exclusive_group(required=False)
    yarn_parser.add_argument("--with-yarn", dest="with_yarn", action="store_true")
    yarn_parser.add_argument("--no-yarn", dest="with_yarn", action="store_false")
    yarn_parser.set_defaults(wiht_yarn=False)

    r_parser = parser.add_mutually_exclusive_group(required=False)
    r_parser.add_argument("--with-r", dest="with_r", action="store_true")
    r_parser.add_argument("--no-r", dest="with_r", action="store_false")
    r_parser.set_defaults(with_r=False)

    parser.add_argument("--output-dir", dest="output_dir", required=True)

    parser.add_argument("--docker-prefix", dest="docker_prefix", default="zero323")
    parser.add_argument("--docker-names", dest="docker_name", default="spark-sandbox")

    parser.add_argument("--profile", choices=["local", "standalone"], default="local")
    parser.add_argument("--client-entrypoint",
                        choices=["spark-submit", "spark-shell", "pyspark", "sparkR"],
                        default="spark-submit")

    make_box(parser.parse_args())
