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

# 3rd party modules
import nose.tools as ns
import numpy as np

# original modules
from capmoe.cv.searchsimilars import searchsimilars


def test_searchsimilars():
    """Tests if similar features are searched collectly"""
    query_img = {'path': 'query', 'feature': np.array([1.0, 0.0])}
    db_imgs = (
        {'path': '3rd', 'feature': np.array([0.0, 1.0])},
        {'path': '1st', 'feature': np.array([1.0, 0.0])},
        {'path': '2nd', 'feature': np.array([1.0, 0.1])},
    )
    similars = searchsimilars(query_img, db_imgs, max_similars=2)
    ns.eq_(len(similars), 2)
    ns.eq_(similars[0], '1st')
    ns.eq_(similars[1], '2nd')
