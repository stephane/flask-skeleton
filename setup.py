#!/usr/bin/env python

import ast
import re

from setuptools import setup

_version_re = re.compile(r"__version__\s+=\s+(.*)")

PROJECT = "skeleton"

with open(PROJECT + "/__init__.py", "rb") as f:
    version = str(
        ast.literal_eval(_version_re.search(f.read().decode("utf-8")).group(1))
    )

setup(
    name=PROJECT,
    version=version,
    author="Stéphane Raimbault",
    author_email="stephane.raimbault@gmail.com",
    license="BSD 3-clause",
    packages=[PROJECT],
    include_package_data=True,
    install_requires=[
        "Flask~=1.1.1",
        "Flask-SQLAlchemy~=2.4.0",
        "psycopg2-binary~=2.8.3",
        "SQLAlchemy~=1.3.6",
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    classifiers=["Programming Language :: Python :: 3"],
)
