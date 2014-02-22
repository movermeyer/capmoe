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
import numpy as np

# original modules
import capmoe.util.logger


# global variables
logger = capmoe.util.logger.factory(__file__)


def bof(features, n_visualwords, flann, flann_index_param, norm_order=None,
        loglevel='WARNING'):
    """Create BoF representation from features & visual words.

    ANN algorithm is internally used. So the result BoF representation is
    approximation.

    :param features: N-dimension array of feature vector
    :type features: N x len(feature) `numpy.ndarray`,
        where each element is `numpy.float32`
    :param n_visualwords: number of visual words
        (necessary to create histogram)
    :param flann: flann object bound to visual words index.
        Got from `flann.FLANN().build_index` or `flann.FLANN().load_index`
    :param flann_index_param: result of `flann.FLANN().build_index`
    :param norm_order: `1` for L1-norm, `2` for L2-norm, ...
        Histogram is not normalized when this is `None`.
    """
    # nearest neighbor search
    t0 = time.time()
    nn_idx, dists = flann.nn_index(
        features, 1, checks=flann_index_param['checks'])
    logger.debug('%f sec to search approx nearest neighbor' %
                 (time.time() - t0))

    # make BoF histogram
    bof_hist, bins = np.histogram(nn_idx, bins=n_visualwords)
    if norm_order is None:
        return bof_hist
    return bof_hist / np.linalg.norm(bof_hist, ord=norm_order)
