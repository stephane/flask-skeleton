#!/usr/bin/env python

import ast
import pip
import re

from pip.req import parse_requirements
from setuptools import setup

_version_re = re.compile(r'__version__\s+=\s+(.*)')

PROJECT = 'skeleton'

with open(PROJECT + '/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

requirements = parse_requirements('requirements.txt', session=pip.download.PipSession())
install_requires = [str(r.req) for r in requirements]

setup(
    name=PROJECT,
    version=version,
    author="Stéphane Raimbault",
    author_email="stephane.raimbault@gmail.com",
    license="BSD 3-clause",
    packages=[PROJECT],
    include_package_data=True,
    install_requires=install_requires,
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
