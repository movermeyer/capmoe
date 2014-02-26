# -*- coding: utf-8 -*-
"""
    :synopsis: Test API to create BoF.

    Description.
"""


# python 2.x support
from __future__ import division, print_function, absolute_import, unicode_literals

# standard modules
import os

# 3rd party modules
from nose_parameterized import parameterized
import numpy as np

# original modules
from capmoe.cv.bof import BoFMaker


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
INDEX_FILE_PATH = 'test_bof_index.dat'

# global variables
## BoF should be created only once
bof = BoFMaker(VISUALWORDS, algorithm='kdtree', loglevel='DEBUG')


def teardown():
    os.remove(INDEX_FILE_PATH)
    os.remove(BoFMaker.meta_filepath(INDEX_FILE_PATH))


@parameterized([
    (None, [3    , 1    , 2    ]),  # v1:3, v2:1, v3:2
    (1   , [0.500, 0.166, 0.333]),  # L1-norm
    (2   , [0.801, 0.267, 0.534]),  # L2-norm
])
def test_bof(norm_order, answer_bof):
    """Test if BoF is created correctly"""
    bof_hist = bof.make(FEATURES, norm_order=norm_order)
    np.testing.assert_array_almost_equal(
        bof_hist, np.array(answer_bof),
        decimal=3)


def test_save_load_index():
    """Test loading/saving index"""
    bof.save(INDEX_FILE_PATH)
    bof2 = BoFMaker(VISUALWORDS, index_filepath=INDEX_FILE_PATH,
                    loglevel='DEBUG')
    bof_hist = bof2.make(FEATURES)
    np.testing.assert_array_equal(bof_hist, np.array([3, 1, 2]))
