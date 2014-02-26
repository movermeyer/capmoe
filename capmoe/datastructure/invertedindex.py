# -*- coding: utf-8 -*-
"""
    capmoe.datastructure.invertedindex
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :synopsis: Provides implementations of inverted index.
"""


# python 2.x support
from __future__ import division, print_function, absolute_import, unicode_literals

# standard modules

# 3rd party modules
import redis

# original modules


class InvertedIndexRedis(object):
    """Inverted index whose backend is Redis.

    ``redis`` module is used as backend.

    Very specific class:
    Only methods necesarry for BoF inverted index are provided.
    """

    def __init__(self, **kw):
        """Connect to Redis server.

        :param kw: passed to `redis.StrictRedis`
        """
        self._redis = redis.StrictRedis(**kw)

    def addhash(self, name, key, value):
        """Adds ``key`` & ``value`` pair into ``name`` record"""
        self._redis.hset(name, key, value)

    def getdict(self, name):
        """Get value of ``name`` record"""
        record = self._redis.hgetall(name)
        return {k: float(v) for k, v in record.items()}
