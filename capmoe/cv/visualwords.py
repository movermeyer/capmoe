# -*- coding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    :synopsis: What is this module for?

    Description.
"""


# python 2.x support
from __future__ import division, print_function, absolute_import, unicode_literals

# standard modules
import time
import itertools

# 3rd party modules
import numpy as np

# original modules
import capmoe.util.logger


# global variables
logger = capmoe.util.logger.factory(__file__)


def visualwords_union(features, loglevel='WARNING'):
    """Create simple visual words just by making union of feature vectors

    Not suitable for large number of features.

    :param features: feature vectors. Iterable of 2-D `numpy.ndarray`.
        Example:

        .. code-block: python

            (
                [[1.2, 3.5], [2.3, 4.1]],  # image0's feature vectors
                ...
            )
    :rtype: 2-D `numpy.ndarray`
    """
    t0 = time.time()
    visualwords = np.array(list(itertools.chain.from_iterable(features)))
    logger.debug('%f sec to union feature vectors' % (time.time() - t0))
    return visualwords
