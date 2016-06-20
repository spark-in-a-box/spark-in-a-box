#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function)

import os
import sys

from sparkinabox.release import __author__, __version__
from sparkinabox.render import render_docker


def main(args):
    if os.path.exists(args.output_dir):
        print("Output directory {0} already exists. Exiting.".format(args.output_dir))
        sys.exit(1)

    for target in ["base", "client", "master", "worker"]:
        basedir = os.path.join(args.output_dir, target)
        os.makedirs(basedir)
        with open(os.path.join(basedir, "Dockerfile"), "w") as fw:
            fw.write(render_docker(args, target))
