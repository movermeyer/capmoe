# -*- coding: utf-8 -*-
"""
    capmoe.api
    ~~~~~~~~~~

    :synopsis: APIs used mainly by `CapMoe web service <https://github.com/laysakura/capmoe_web>`_

    This module provides algorithms to search similar beer caps from image files.
    CV algorithms and data structures are (hopefully) highly abstracted.
"""


# python 2.x support
from __future__ import division, print_function, absolute_import, unicode_literals

# standard modules

# 3rd party modules

# original modules
from capmoe.cv.capdetector import capdetector
from capmoe.cv.searchsimilars import searchsimilars
