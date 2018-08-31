# -*- coding: utf-8 -*-

"""
This module provides functions for searching the courses
in command line interface by pysaint

"""
from __future__ import absolute_import
import click

import boilerplate


@click.command()
@click.option("--string", "-s", default='Hello World', type=(str, ), )
def single_print(example_string):
    """
    Example Usage

    >> single_print --string="hi there~"
    :return:
    """
    boilerplate.test(example_string)


@click.command()
@click.option("--string", "-s", default='Hello World', type=(str, list, tuple), multiple=True)
def multiple_print(example_string):
    """
    Example Usage

    >> multiple_print --string="hello" --string="world"
    :param example_string:
    :return:
    """
    boilerplate.test("\n".join(example_string))

