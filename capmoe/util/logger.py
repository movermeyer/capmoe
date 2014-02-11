# -*- coding: utf-8 -*-
"""
    capmoe.util.logger
    ~~~~~~~~~~~~~~~~~~

    :synopsis: Provides rainbow logger

    Description.
"""


# python 2.x support
from __future__ import division, print_function, absolute_import, unicode_literals

# standard modules
import logging
import sys

# 3rd party modules
from rainbow_logging_handler import RainbowLoggingHandler

# original modules


def factory(logger_name):
    """Logger factory
    """
    logger = logging.getLogger(logger_name)
    handler = RainbowLoggingHandler(sys.stderr, datefmt=None)
    handler.setFormatter(logging.Formatter("[%(asctime)s] %(filename)s %(funcName)s():%(lineno)d\t%(message)s"))
    logger.addHandler(handler)
    return logger
