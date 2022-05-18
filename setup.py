# !/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

setup(
    name='gpio-over-wamp',
    version='1.0',
    description='Turns the light on/off over wamp(crossbar) using Raspberry pi',
    author='CODEBASE PK',
    packages=find_packages(),
    scripts=['gpiowamp']
)