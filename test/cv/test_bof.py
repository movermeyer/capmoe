# -*- coding: utf-8 -*-
"""
    :synopsis: Test API to create BoF.

    Description.
"""


# python 2.x support
from __future__ import division, print_function, absolute_import, unicode_literals

# standard modules

# 3rd party modules
from nose_parameterized import parameterized
import numpy as np
import pyflann

# original modules
from capmoe.cv.bof import bof


# constants
VISUALWORDS = np.array([
    [1.0, 0.0, 0.0],  # v1
    [0.0, 1.0, 0.0],  # v2
    [0.0, 0.0, 1.0],  # v3
])
FEATURES = np.array([
    #                 # nearest neighbor
    [2.0, 0.1, 0.0],  # v1
    [1.0, 0.5, 0.5],  # v1
    [0.5, 0.4, 0.4],  # v1
    [0.0, 1.0, 0.0],  # v2
    [0.9, 0.9, 1.0],  # v3
    [0.2, 0.1, 1.5],  # v3
])


@parameterized([
    (None, [3    , 1    , 2    ]),  # v1:3, v2:1, v3:2
    (1   , [0.500, 0.166, 0.333]),  # L1-norm
    (2   , [0.801, 0.267, 0.534]),  # L2-norm
])
def test_bof(norm_order, answer_bof):
    """Test if BoF is created correctly"""
    flann = pyflann.FLANN()
    param = flann.build_index(VISUALWORDS, algorithm='kdtree')

    bof_ = bof(FEATURES, VISUALWORDS.shape[0], flann, param,
               norm_order=norm_order, loglevel='DEBUG')
    np.testing.assert_array_almost_equal(
        bof_, np.array(answer_bof),
        decimal=3)
