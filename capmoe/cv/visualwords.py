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
import itertools

# 3rd party modules
import numpy as np

# original modules


def visualwords_union(features):
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
    return np.array(list(itertools.chain.from_iterable(features)))
