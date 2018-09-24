#!/usr/bin/env python3

from setuptools import setup

setup(
    name='litcoin',
    version='0.0.0',
    description='A library for interacting with Bitcoin and Litecoin',
    license='MIT',
    packages=['litcoin'],
    author='Noel ODonnell',
    keywords=['bitcoin', 'litecoin', 'litcoin'],
    url='https://github.com/odonnellnoel/litcoin',

    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)
