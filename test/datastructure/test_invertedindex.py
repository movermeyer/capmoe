# -*- coding: utf-8 -*-
"""
    :synopsis: Test inverted index

    Description.
"""


# python 2.x support
from __future__ import division, print_function, absolute_import, unicode_literals

# standard modules

# 3rd party modules
import nose.tools as ns

# original modules
from capmoe.datastructure.invertedindex import InvertedIndexRedis


def test_inverted_index_redis():
    """Test Redis inverted index.

    Redis server must be running on localhost:6379 to pass this test.
    Only methods necesarry for BoF inverted index are tested.
    """
    ii = InvertedIndexRedis(host='localhost', port=6379)

    ii.addhash('vw:0', 'im:0', 0.72)
    ii.addhash('vw:0', 'im:3', 0.01)
    ns.eq_(ii.getdict('vw:0'), {'im:0': 0.72, 'im:3': 0.01})

    ii.addhash('vw:0', 'im:0', 0.44)
    ns.eq_(ii.getdict('vw:0'), {'im:0': 0.44, 'im:3': 0.01})
