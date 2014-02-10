#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup


tests_require = [
    'nose',
    'coverage',
    'nose-cov',
    'nose-parameterized',
],

setup(
    name             = 'capmoe',
    description      = 'CapMoe - Cap Beer cap image search, CLI tools',
    long_description = open('README.rst').read(),
    url              = 'https://github.com/laysakura/capmoe',
    # license          = 'LICENSE.txt',
    version          = '0.0.1',
    author           = 'Sho Nakatani',
    author_email     = 'lay.sakura@gmail.com',
    tests_require    = tests_require,
    install_requires = [
        'pillow',
        'scipy',
        'numpy',
        'simplejson',
    ],
    extras_require = {
        'testing': tests_require,
    },
    packages = [
        'capmoe',
        'capmoe.api',
        'capmoe.cv',
    ],
    scripts = [
        'bin/capmoe-capdetector.py',
    ],
    classifiers = '''
Programming Language :: Python
Development Status :: 1 - Planning
Programming Language :: Python :: 2.7
Operating System :: POSIX :: Linux
'''.strip().splitlines()
)
