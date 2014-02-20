# -*- coding: utf-8 -*-
"""
    capmoe.cv.searchsimilars
    ~~~~~~~~~~~~~~~~~~~~~~~~

    :synopsis: Searches images similar to query from database.

    Description.
"""


# python 2.x support
from __future__ import division, print_function, absolute_import, unicode_literals

# standard modules

# 3rd party modules
import numpy as np

# original modules
import capmoe.util.logger
from capmoe.util.collections import fixedlen_ordered_list


# global variables
logger = capmoe.util.logger.factory(__file__)


def _distance(feature0, feature1):
    """Euclidean distance is currently used"""
    return np.power(feature0 - feature1, 2).sum()


def searchsimilars(query_img, db_imgs,
                   max_similars, loglevel='WARNING'):
    """Search images similar to query image from db image

    :type query_img: {'path': '/path/to/img', 'fearture': `narray` feature vector}
    :type db_imgs: iterable of {'path': '/path/to/img', 'fearture': `narray` feature vector}
    :rtype: (<similar image path>, ...) w/
        length less than :param:`max_candidates`.
        Left element has higher similarity.
    """
    similars = fixedlen_ordered_list(
        maxlen=max_similars, key=lambda e: e['similarity'])
    for db_img in db_imgs:
        d = _distance(query_img['feature'], db_img['feature'])
        similars.append({'path': db_img['path'], 'similarity': -d})

    return tuple([similar['path'] for similar in similars])
