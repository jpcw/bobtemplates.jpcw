#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Render bobtemplates.jpcw hooks.
"""

__docformat__ = 'restructuredtext en'


import os
from mrbob.bobexceptions import ValidationError
from datetime import date



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


def valid_pkg_license(configurator, question, answer):
    """Check license answer."""
    licenses = ['BSD', 'GPL']
    if answer.upper().strip() not in licenses:
        raise ValidationError("'{0}' is not in {1}".format(answer, licenses))
    return answer


def clean_gpl(configurator):
    """Clean License if needed."""
    if configurator.variables['pkg_license'] == 'BSD':
        gpl = os.path.join(configurator.target_directory, 'docs', 'LICENSE.gpl')
        if os.path.isfile(gpl):
            os.remove(gpl)


def basic_namespace_pre_render(configurator):
    """License stuff."""
    other_vars = {'year': date.today().year}
    configurator.variables.update(other_vars)


def basic_namespace_post_render(configurator):
    """Clean License if needed."""
    clean_gpl(configurator)


# vim:set et sts=4 ts=4 tw=80:
