#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'requests'
]

test_requirements = [
    'requests'
]

setup(
    name='dteenergybridge',
    version='0.1.1',
    description="Library for retrieving data from a DTE Energy Bridge",
    long_description=readme + '\n\n' + history,
    author="Kyle John Hendricks",
    author_email='kyle@hendricks.nu',
    url='https://github.com/kylehendricks/dteenergybridge',
    packages=find_packages(include=['dteenergybridge']),
    include_package_data=True,
    install_requires=requirements,
    test_requires=test_requirements,
    license="MIT license",
    zip_safe=False,
    keywords='dteenergybridge',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
)
