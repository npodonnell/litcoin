#!/usr/bin/env python3

from setuptools import setup

setup(
    name="litcoin",
    version="0.0.1",
    description="A library for interacting with Bitcoin and Litecoin",
    license="MIT",
    packages=["litcoin", "litcoin.script"],
    author="N. P. O\'Donnell",
    keywords=["bitcoin", "litecoin", "litcoin"],
    url="https://github.com/npodonnell/litcoin",
    test_suite="tests",
    tests_require=[
        "mock",
        "pytest",
        "pytest-runner"
    ]
)
