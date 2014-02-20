# -*- coding: utf-8 -*-
"""
    capmoe.util.collections
    ~~~~~~~~~~~~~~~~~~~~~~~

    :synopsis: Provides useful collections

    Description.
"""


# python 2.x support
from __future__ import division, print_function, absolute_import, unicode_literals

# standard modules

# 3rd party modules

# original modules


class fixedlen_ordered_list(list):
    """Creates fixed-length & ordered list.

    Left element is larger.

    :params maxlen: max length of list
    :params key: same as `key` of builtin `sorted()`

    *Example*

    .. code-block: python
        >>> l = fixedlen_ordered_list(maxlen=3)
        >>> l
        []
        >>> l.append(10)
        >>> l.append(9)
        >>> l.append(11)
        >>> l.append(12)
        >>> l
        [12, 11, 10]
        >>> l.append(12)
        >>> l.append(12)
        >>> l
        [12, 12, 12]
        >>> l = fixedlen_ordered_list(maxlen=2, key=lambda e: e[1])
        >>> l
        []
        >>> l.append((0, 18))
        >>> l.append((0, 16))
        >>> l.append((0, 25))
        >>> l
        [(0, 25), (0, 18)]
    """

    def __init__(self, maxlen, key=None):
        self._maxlen = maxlen
        self._key    = key
        list.__init__(self)

    def append(self, x):
        list.append(self, x)
        self.sort(key=self._key, reverse=True)
        if len(self) > self._maxlen:
            del self[self._maxlen]

    def __add__(self):
        raise NotImplementedError('Use `append()`')

    def extend(self):
        raise NotImplementedError('Use `append()`')

    def insert(self):
        raise NotImplementedError('Use `append()`')

    def reverse(self):
        raise NotImplementedError('method not supported')
