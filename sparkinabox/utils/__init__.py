#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division, absolute_import
import re

import requests


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