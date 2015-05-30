# !/usr/bin/env python
# coding: utf-8
# setup.py - 14-10-3
__author__ = 'winkidney'

import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

requires = [
    'django>=1.8.0',
]

setup(
    name='weixin2py',
    version='0.1.3',
    packages=find_packages('.', exclude=("wei_demo", )),
    install_requires=requires,
)