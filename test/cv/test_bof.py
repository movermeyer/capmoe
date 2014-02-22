# -*- coding: utf-8 -*-
"""
    :synopsis: Test API to create BoF.

    Description.
"""


# python 2.x support
from __future__ import division, print_function, absolute_import, unicode_literals

# standard modules

# 3rd party modules
import numpy as np

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


def test_bof():
    """Test if BoF is created correctly"""
    bof_ = bof(FEATURES, VISUALWORDS, loglevel='DEBUG')
    np.testing.assert_array_equal(
        bof_, np.array([3, 1, 2]))  # v1:3, v2:1, v3:2


def test_bof_normalized():
    """Test if BoF is correctly normalized"""
    # L1-norm
    bof_ = bof(FEATURES, VISUALWORDS, norm_order=1, loglevel='DEBUG')
    np.testing.assert_array_almost_equal(
        bof_, np.array([0.500, 0.166, 0.333]),
        decimal=3)

    # L2-norm
    bof_ = bof(FEATURES, VISUALWORDS, norm_order=2, loglevel='DEBUG')
    np.testing.assert_array_almost_equal(
        bof_, np.array([0.801, 0.267, 0.534]),
        decimal=3)
