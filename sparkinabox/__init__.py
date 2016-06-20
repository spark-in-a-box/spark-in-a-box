#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function)

import os
import sys

from jinja2 import PackageLoader, Environment

from sparkinabox.release import __author__, __version__
from sparkinabox.utils import closest_apache_mirror, anaconda_url, anaconda_installer, mvn_params, normalize_blanklines


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
    if os.path.exists(args.output_dir):
        print("Output directory {0} already exists. Exiting.".format(args.output_dir))
        sys.exit(1)

    basedir = os.path.join(args.output_dir, "base")
    os.makedirs(basedir)

    with open(os.path.join(basedir, "Dockerfile"), "w") as fw:
        fw.write(render_base(args))
