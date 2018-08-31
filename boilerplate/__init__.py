# -*- coding: utf-8 -*-
from __future__ import absolute_import

from pkg_resources import get_distribution

from boilerplate.api import test, login

__version__ = get_distribution('boilerplate').version

__all__ = [
    'test',
    'login',
]
