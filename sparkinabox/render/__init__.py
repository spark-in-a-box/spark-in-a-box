#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division, absolute_import

from jinja2 import Environment, PackageLoader

from sparkinabox.utils import closest_apache_mirror, mvn_params, anaconda_installer, anaconda_url, normalize_blanklines


def render_docker(args, target="base"):
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
        "DOCKER_PREFIX": args.docker_prefix,
        "DOCKER_NAME": args.docker_name
    }

    return normalize_blanklines(env.get_template("{0}.Dockerfile".format(target)).render(defaults))
