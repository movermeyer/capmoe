# -*- coding: utf-8 -*-
"""
    capmoe.cv.bof
    ~~~~~~~~~~~~~

    :synopsis: Create BoF representation from features & visual words
"""


# python 2.x support
from __future__ import division, print_function, absolute_import, unicode_literals

# standard modules
import time

# 3rd party modules
import numpy as np
import pyflann
import simplejson as json

# original modules
import capmoe.util.logger


# global variables
logger = capmoe.util.logger.factory(__file__)


class BoFMaker(object):
    """Create BoF representation from features & visual words.

    Since ANN algorithm is used internally,
    the result BoF representation is approximation.

    Index creation is wrapped by this class.
    """

    def __init__(self, visualwords,
                 index_filepath=None,
                 algorithm='kdtree',
                 loglevel='WARNING'):
        """Create or load index of visual words.

        :param visualwords: 2D array of base vectors
        :type visualwords: M x len(feature) `numpy.ndarray`,
            where each element is `numpy.float32`
        :param index_filepath: If not `None`, index is not created
           but load from specified file.
           The file must be created by :func:`BoFMaker.save`
        :param algorithm: passed to `pyflann.FLANN().build_index`
        """
        self._n_visualwords = visualwords.shape[0]
        self._flann         = pyflann.FLANN()

        if index_filepath is not None:
            # load index
            logger.debug('Loading visual words index from %s ...' %
                         (index_filepath))
            t0 = time.time()
            with open(BoFMaker.meta_filepath(index_filepath)) as f:
                self._index_param = json.load(f)
            self._flann.load_index(index_filepath, visualwords)
            logger.debug('%f sec to load index' % (time.time() - t0))
        else:
            # create index
            logger.debug('Creating index of visual words...')
            t0 = time.time()
            self._index_param = self._flann.build_index(
                visualwords, algorithm=algorithm)
            logger.debug('%f sec to create index' % (time.time() - t0))

    def save(self, filepath):
        """Save index of visual words to ``filepath``"""
        with open(BoFMaker.meta_filepath(filepath), 'w') as f:
            json.dump(self._index_param, f)
        self._flann.save_index(filepath)

    def make(self, features, norm_order=None):
        """Create BoF representation of features.

        :param features: 2D array of feature vectors
        :type features: N x len(feature) `numpy.ndarray`,
            where each element is `numpy.float32`
        :param norm_order: `1` for L1-norm, `2` for L2-norm, ...
            Histogram is not normalized when this is `None`.
        """
        # nearest neighbor search
        t0 = time.time()
        nn_idx, dists = self._flann.nn_index(
            features, 1, checks=self._index_param['checks'])
        logger.debug('%f sec to search approx nearest neighbor' %
                     (time.time() - t0))

        # make BoF histogram
        bof_hist, bins = np.histogram(nn_idx, bins=self._n_visualwords)
        if norm_order is None:
            return bof_hist
        return bof_hist / np.linalg.norm(bof_hist, ord=norm_order)

    @staticmethod
    def meta_filepath(index_filepath):
        """Generate path to meta data file"""
        return '%s-meta.json' % (index_filepath)
