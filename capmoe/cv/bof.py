# -*- coding: utf-8 -*-
"""
    capmoe.cv.bof
    ~~~~~~~~~~~~~

    :synopsis: Create BoF representation from features & visual words

    Description.
"""


# python 2.x support
from __future__ import division, print_function, absolute_import, unicode_literals

# standard modules
import time

# 3rd party modules
import pyflann
import numpy as np

# original modules
import capmoe.util.logger


# global variables
logger = capmoe.util.logger.factory(__file__)


def bof(features, visualwords, norm_order=None, loglevel='WARNING'):
    """Create BoF representation from features & visual words.

    ANN algorithm is internally used. So the result BoF representation is
    approximation.

    :param features: N-dimension array of feature vector
    :type features: N x len(feature) `numpy.ndarray`,
        where each element is `numpy.float32`
    :param visualwords: M-dimension array of base vector
    :type visualwords: M x len(feature) `numpy.ndarray`,
        where each element is `numpy.float32`
    :param norm_order: `1` for L1-norm, `2` for L2-norm, ...
        Histogram is not normalized when this is `None`.
    """
    flann = pyflann.FLANN()

    # build index
    # [todo] - save & reuse index
    t0 = time.time()
    params = flann.build_index(visualwords, algorithm='kdtree')
    logger.debug('%f sec to build flann index flann index' %
                 (time.time() - t0))
    logger.debug('params: %s' % (params))

    # nearest neighbor search
    t0 = time.time()
    result, dists = flann.nn_index(features, 1, checks=params['checks'])
    logger.debug('%f sec search approx nearest neighbor' % (time.time() - t0))

    # make BoF histogram
    n_visualwords = visualwords.shape[0]
    bof_hist, bins = np.histogram(result, bins=n_visualwords)
    if norm_order is None:
        return bof_hist
    return bof_hist / np.linalg.norm(bof_hist, ord=norm_order)
