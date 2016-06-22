#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division, absolute_import
import os

from jinja2 import Environment, PackageLoader

from sparkinabox.utils import normalize_blanklines


_env = Environment(loader=PackageLoader('sparkinabox', 'templates'))


def render_docker(context, target="base"):
    return normalize_blanklines(_env.get_template(
        os.path.join("dockerfiles", "{0}.Dockerfile".format(target))
    ).render(context))


def render_make(context):
    return _env.get_template(
        os.path.join("compose", "Makefile")
    ).render(context)
