#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Render bobtemplates.jpcw hooks.
"""

__docformat__ = 'restructuredtext en'


import os


def basicnamespace_pre_pkg_ns(configurator, question):
    """Guess default pkg_ns from Output Directory"""
    names = configurator.target_directory.split(os.sep)[-1].split('.')
    if len(names) == 2:
       question.default = names[0]


def basicnamespace_pre_pkg_project(configurator, question):
    """Guess default pkg_project from Output Directory"""
    names = configurator.target_directory.split(os.sep)[-1].split('.')
    if len(names) == 2:
        question.default = names[1]


# vim:set et sts=4 ts=4 tw=80:
