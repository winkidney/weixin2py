# !/usr/bin/env python
# coding: utf-8
# setup.py - 14-10-3
__author__ = 'winkidney'
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

requires = [
    'django',
]

setup(name='weixin2py',
      version='0.1.1',
      packages=find_packages(here),
      requires=requires,
     )