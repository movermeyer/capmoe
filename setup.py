#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name             = 'capmoe',
    description      = 'CapMoe - Cap crown searcher',
    long_description = open('README.rst').read(),
    url              = 'https://github.com/laysakura/capmoe',
    license          = 'LICENSE.txt',
    version          = '0.0.1',
    author           = 'Sho Nakatani',
    author_email     = 'lay.sakura@gmail.com',
    install_requires = [
        'pillow',
    ],
    tests_require    = [
        'nose',
        'coverage',
        'nose-cov',
    ],
    packages         = [
        'capmoe',
    ],
    scripts          = [
    ],
    classifiers      = '''
Programming Language :: Python
Development Status :: 1 - Planning
License :: OSI Approved :: BSD License
Programming Language :: Python :: 3.2
Programming Language :: Python :: 3.3
'''.strip().splitlines()
)
