#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division, absolute_import

import os
import sys

from sparkinabox.render import render_docker


targets = {
    "local": ["base", "client"],
    "standalone": ["base", "client", "master", "worker"]
}


def make_box(args):
    if os.path.exists(args.output_dir):
        print("Output directory {0} already exists. Exiting.".format(args.output_dir))
        sys.exit(1)

    for target in targets[args.profile]:
        basedir = os.path.join(args.output_dir, target)
        os.makedirs(basedir)
        with open(os.path.join(basedir, "Dockerfile"), "w") as fw:
            fw.write(render_docker(args, target))
