# -*- coding: utf-8 -*-
"""
    :synopsis: Tests visual words construction

    Description.
"""


# python 2.x support
from __future__ import division, print_function, absolute_import, unicode_literals

# standard modules

# 3rd party modules
from nose_parameterized import parameterized
import numpy as np

# original modules
from capmoe.cv.visualwords import visualwords_union


@parameterized([
    (
        [
            [[1, 2], [3, 4]],
            [[5, 6], [7, 8]],
        ],
        [[1, 2], [3, 4], [5, 6], [7, 8]]
    )
])
def test_visualwords_union(features, results):
    """Test simple visual words by union"""
    vw = visualwords_union([np.array(feature) for feature in features])
    np.testing.assert_array_equal(vw, np.array(results))
