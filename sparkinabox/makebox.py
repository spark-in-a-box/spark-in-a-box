#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division, absolute_import

import os
import sys

from sparkinabox.render import render_docker, render_make
from sparkinabox.utils import closest_apache_mirror, mvn_params, anaconda_installer
from sparkinabox.compose import make_compose

targets = {
    "local": ["base", "client"],
    "standalone": ["base", "client", "master", "worker"]
}

DUMB_INIT_VERSION = "1.2.2"


def make_context(args):
    apache_mirror = closest_apache_mirror()
    return {
        "USERNAME": args.username,
        "JDK_VERSION": args.jdk,
        "PYTHON_VERSION": args.python,
        "SCALA_VERSION": args.scala,
        "SPARK_VERSION": args.spark,
        "HADOOP_FULL_VERSION": args.hadoop_version,
        "HADOOP_MAJOR_VERSION": "{0}.{1}".format(*args.hadoop_version.split(".")),
        "APACHE_MIRROR": closest_apache_mirror(),
        "SPARK_DIST_URL": "{0}/spark".format(apache_mirror),
        "HADOOP_DIST_URL": "{0}/hadoop/common".format(apache_mirror),
        "MVN_PARAMS": mvn_params(args),
        "ANACONDA_INSTALLER": anaconda_installer(args.anaconda_version, args.python),
        "ANACONDA_URL": args.anaconda_repository,
        "PYTHON_HASHSEED": args.python_hashseed,
        "PYTHON_PACKAGES":  "{0}{1}".format("nomkl " if args.nomkl else "", args.python_packages),
        "HADOOP_PROVIDED": args.hadoop_provided,
        "WITH_R": args.with_r,
        "DOCKER_PREFIX": args.docker_prefix,
        "DOCKER_NAME": args.docker_name,
        "CLIENT_ENTRYPOINT": args.client_entrypoint,
        "PROFILE": args.profile,
        "MVN_ARTIFACTS": args.mvn_artifacts,
        "DUMB_INIT_VERSION": DUMB_INIT_VERSION,
    }


def make_box(args):
    context = make_context(args)

    if os.path.exists(args.output_dir):
        print("Output directory {0} already exists. Exiting.".format(args.output_dir))
        sys.exit(1)

    for target in targets[args.profile]:
        basedir = os.path.join(args.output_dir, target)
        os.makedirs(basedir)
        with open(os.path.join(basedir, "Dockerfile"), "w") as fw:
            fw.write(render_docker(context, target))

    with open(os.path.join(args.output_dir, "Makefile"), "w") as fw:
        fw.write(render_make(context))

    with open(os.path.join(args.output_dir, "docker-compose.yml"), "w") as fw:
        fw.write(make_compose(context, targets[args.profile]))
