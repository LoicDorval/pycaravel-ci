#! /usr/bin/env python
##########################################################################
# NSAp - Copyright (C) CEA, 2019
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html
# for details.
##########################################################################


# System import
from __future__ import print_function
import os
import re
import sys
import platform
import subprocess
from pprint import pprint
from distutils.version import LooseVersion
from setuptools.command.build_ext import build_ext
from setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommand


# Package information
release_info = {}
infopath = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "caravel", "info.py"))
with open(infopath) as open_file:
    exec(open_file.read(), release_info)
pkgdata = {
    "caravel": [
        os.path.join("conf", "*.conf")]
}

# Write setup
setup(
    name=release_info["NAME"],
    description=release_info["DESCRIPTION"],
    long_description=release_info["LONG_DESCRIPTION"],
    license=release_info["LICENSE"],
    classifiers=release_info["CLASSIFIERS"],
    author=release_info["AUTHOR"],
    author_email=release_info["AUTHOR_EMAIL"],
    version=release_info["VERSION"],
    url=release_info["URL"],
    packages=find_packages(exclude="doc"),
    platforms=release_info["PLATFORMS"],
    extras_require=release_info["EXTRA_REQUIRES"],
    install_requires=release_info["REQUIRES"],
    package_data=pkgdata,
    scripts=release_info["SCRIPTS"]
)
