#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division, absolute_import

import os

from jinja2 import Environment, PackageLoader

from sparkinabox.utils import normalize_blanklines


def render_docker(context, target="base"):
    env = Environment(loader=PackageLoader('sparkinabox', 'templates'))
    template = env.get_template(os.path.join("dockerfiles", "{0}.Dockerfile".format(target)))

    return normalize_blanklines(env.get_template(template).render(context))
