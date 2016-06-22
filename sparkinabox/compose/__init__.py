#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division, absolute_import

import yaml


def _image(context, role):
    return "{0}/{1}-{2}".format(context["DOCKER_PREFIX"], context["DOCKER_NAME"], role)


def _interactive(context):
    return context["CLIENT_ENTRYPOINT"] != "spark-submit"


def make_client(context):
    return {
        "build": "./client",
        "image": _image(context, "client"),
        "links": ["master"] if context["PROFILE"] != "local" else [],
        "stdin_open": _interactive(context),
        "tty":  _interactive(context),
    }


def make_master(context):
    return {
        "build": "./master",
        "image": _image(context, "master"),
        "ports": ["8080:8080"],
    }


def make_worker(context):
    return {
        "build": "./worker",
        "image": _image(context, "worker"),
        "links": ["master"]
    }


def make_compose(context, targets):
    return yaml.dump({
        "version": "2",
        "services": {target: make(context) for target, make in {
            "master": make_master,
            "worker": make_worker,
            "client": make_client,
        }.items() if target in targets}
    }, default_flow_style=False)
