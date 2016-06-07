#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function)
from sparkinabox.release import __author__, __version__

import requests
import re
from functools import lru_cache
from jinja2 import PackageLoader, Environment


@lru_cache(128)
def closest_apache_mirror(fallback=None):
    """http://stackoverflow.com/q/21534797"""
    r = requests.get("https://www.apache.org/dyn/closer.cgi?as_json=1")
    return (r.json().get("preferred", fallback) if r.ok else fallback).rstrip("/")


def anaconda_url(base_url, anaconda):
    return {"anaconda": "{0}/archive", "miniconda": "{0}/miniconda"}[anaconda].format(base_url)


def anaconda_installer(anaconda, anaconda_version, python_version):
    return {
        "anaconda":  "Anaconda{0}-{1}-Linux-x86.sh",
        "miniconda": "Miniconda{0}-{1}-Linux-x86_64.sh"
    }[anaconda].format(python_version, anaconda_version)


def mvn_params(args):
    return " ".join([param for param in [
        "-Phive -Phive-thriftserver" if args.with_hive else None,
        "-Pyarn" if args.with_yarn else None,
        "-Phadoop-provided" if args.with_hadoop_provided
        else "-Phadoop-{0}.{1} -Dhadoop.version={0}.{1}.{2}".format(*args.hadoop_version.split(".")),
        "-Psparkr" if args.with_r else None
    ] if param])


def normalize_blanklines(s):
    return re.sub(r"\n{3,}", "\n", s)


def render_base(args):
    env = Environment(loader=PackageLoader('sparkinabox', 'templates'))

    defaults = {
        "USERNAME": args.username,
        "JDK_VERSION": args.jdk,
        "PYTHON_VERSION": args.python,
        "SCALA_VERSION": args.scala,
        "SPARK_VERSION": args.spark,
        "HADOOP_FULL_VERSION": args.hadoop_version,
        "HADOOP_MAJOR_VERSION": "{0}.{1}".format(*args.hadoop_version.split(".")),
        "APACHE_MIRROR": closest_apache_mirror(),
        "SPARK_DIST_URL": "{0}/spark".format(closest_apache_mirror()),
        "HADOOP_DIST_URL": "{0}/hadoop/common".format(closest_apache_mirror()),
        "MVN_PARAMS": mvn_params(args),
        "ANACONDA_INSTALLER": anaconda_installer(args.anaconda, "latest", args.python),
        "ANACONDA_URL": anaconda_url(args.anaconda_repository, args.anaconda),
        "PYTHON_HASHSEED": args.python_hashseed,
        "PYTHON_PACKAGES":  "{0}{1}".format("nomkl " if args.nomkl else "", args.python_packages),
        "HADOOP_PROVIDED": args.hadoop_provided,
        "WITH_R": args.with_r,
    }

    return normalize_blanklines(env.get_template("Dockerfile").render(defaults))


def main(args):
    return render_base(args)



