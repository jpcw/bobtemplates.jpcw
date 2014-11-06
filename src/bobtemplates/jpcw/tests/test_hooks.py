#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Doc here.
"""

__docformat__ = 'restructuredtext en'

import os
import shutil
import tempfile

from datetime import date
from unittest import TestCase


class DummyConfigurator(object):
    def __init__(self,
                 defaults=None,
                 bobconfig=None,
                 templateconfig=None,
                 variables=None,
                 quiet=False):
        self.defaults = defaults or {}
        self.bobconfig = bobconfig or {}
        self.variables = variables or {}
        self.quiet = quiet
        self.templateconfig = templateconfig or {}


class Basic_NamespaceTest(TestCase):

    def setUp(self):
        self.target_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.target_dir)

    def call_FUT(self, *args, **kw):
        from mrbob.configurator import Configurator
        return Configurator(*args, **kw)

    def test_ns_pkg(self):
        from ..hooks import basicnamespace_pre_pkg_ns
        from ..hooks import basicnamespace_pre_pkg_project
        configurator = self.call_FUT('bobtemplates.jpcw:basic_namespace',
                                     'mynamespace.mypkg', {})
        self.assertEquals(configurator.questions[0].default, None)
        basicnamespace_pre_pkg_ns(configurator, configurator.questions[0])
        self.assertEquals(configurator.questions[0].default, 'mynamespace')

        self.assertEquals(configurator.questions[1].default, None)
        basicnamespace_pre_pkg_project(configurator, configurator.questions[1])
        self.assertEquals(configurator.questions[1].default, 'mypkg')

    def test_basic_namespace_pre_render(self):
        from ..hooks import basic_namespace_pre_render
        configurator = self.call_FUT('bobtemplates.jpcw:basic_namespace',
                                     'mynamespace.mypkg',
                                     variables={'pkg_license': 'BSD'})
        basic_namespace_pre_render(configurator)
        self.assertEquals(configurator.variables['year'], date.today().year)

    def test_basic_namespace_post_render_gpl(self):

        from ..hooks import basic_namespace_post_render
        tpl_vars = {'pkg_license': 'GPL', 'gpl': 'y', 'pkg_ns': 'mytruc',
                    'pkg_keywords': 'Python', 'pkg_author_name': 'me',
                    'pkg_author_email': 'me@.tld', 'pkg_url': 'http://.tld',
                    'pkg_zipsafe': 'false', 'year': 2013, 'pkg_project': 'my',
                    'pkg_description': 'testing my templates',
                    'pkg_travis': 'y', 'pkg_nose': 'y', 'pkg_coverage': 'y',
                    'pkg_coveralls': 'y', 'dcvs_nick': 'jpcw',
                    'forgeurl': 'https://github.com', 'pkg_sphinx': 'y',
                    'pkg_sphinx_contrib_gen_node': 'y',
                    'pkg_zest_releaser': 'y',
                    'git_gitignore': 'f',
                    'buildout_buildout': 'f',
                    'buildout_bootstrap': 'f'
                    }
        configurator = self.call_FUT('bobtemplates.jpcw:basic_namespace',
                                     'mynamespace.mypkg',
                                     variables=tpl_vars)
        configurator.target_directory = self.target_dir
        configurator.render()
        basic_namespace_post_render(configurator)
        self.assertTrue(os.path.exists('%s/%s' % (self.target_dir,
                                        'docs/LICENSE.GPL')))

    def test_basic_namespace_post_render_bsd(self):

        from ..hooks import basic_namespace_post_render
        tpl_vars = {'pkg_license': 'BSD', 'gpl': 'y', 'pkg_ns': 'mytruc',
                    'pkg_keywords': 'Python', 'pkg_author_name': 'me',
                    'pkg_author_email': 'me@.tld', 'pkg_url': 'http://.tld',
                    'pkg_zipsafe': 'false', 'year': 2013, 'pkg_project': 'my',
                    'pkg_description': 'testing my templates',
                    'pkg_travis': 'y', 'pkg_nose': 'y', 'pkg_coverage': 'y',
                    'pkg_coveralls': 'y', 'dcvs_nick': 'jpcw',
                    'forgeurl': 'https://github.com', 'pkg_sphinx': 'y',
                    'pkg_sphinx_contrib_gen_node': 'y',
                    'pkg_zest_releaser': 'y',
                    'git_gitignore': 'f',
                    'buildout_buildout': 'f',
                    'buildout_bootstrap': 'f'
                    }
        configurator = self.call_FUT('bobtemplates.jpcw:basic_namespace',
                                     'mynamespace.mypkg',
                                     variables=tpl_vars)
        configurator.target_directory = self.target_dir
        configurator.render()
        self.assertFalse(os.path.exists('%s/%s' % (self.target_dir,
                                        'docs/LICENSE.GPL')))

class valid_pkg_licenseTest(TestCase):

    def call_FUT(self, answer, configurator=None, question=None):
        from ..hooks import valid_pkg_license
        return valid_pkg_license(DummyConfigurator(), question, answer)

    def test_license(self):
        for value in ['BSD', 'bsd', 'GPL', 'gpl']:
            self.assertTrue(self.call_FUT(value.lower()))

    def test_license_wrong_input(self):
        from mrbob.bobexceptions import ValidationError
        self.assertRaises(ValidationError, self.call_FUT, 'foo')


class render_structureTest(TestCase):

    def setUp(self):
        import bobtemplates.jpcw
        self.fs_tempdir = tempfile.mkdtemp()
        base_path = os.path.dirname(bobtemplates.jpcw.__file__)
        self.fs_templates = base_path

    def tearDown(self):
        shutil.rmtree(self.fs_tempdir)

    def call_FUT(self, template, variables, output_dir=None, verbose=True,
                 renderer=None, ignored_files=[], ignored_directories=[]):
        from mrbob.rendering import render_structure
        from mrbob.rendering import jinja2_renderer

        if renderer is None:
            renderer = jinja2_renderer

        render_structure(
            template,
            output_dir,
            variables,
            verbose,
            renderer,
            ignored_files,
            ignored_directories
        )

    def test_render_license_bsd(self):
        from ..hooks import basic_namespace_post_render
        tpl_vars = {'pkg_license': 'BSD', 'gpl': 'n', 'pkg_ns': 'mytruc',
                    'pkg_keywords': 'Python', 'pkg_author_name': 'me',
                    'pkg_author_email': 'me@.tld', 'pkg_url': 'http://.tld',
                    'pkg_zipsafe': 'false', 'year': 2013, 'pkg_project': 'my',
                    'pkg_description': 'testing my templates',
                    'pkg_travis': 'y', 'pkg_nose': 'y', 'pkg_coverage': 'y',
                    'pkg_coveralls': 'y', 'dcvs_nick': 'jpcw',
                    'forgeurl': 'https://github.com', 'pkg_sphinx': 'y',
                    'pkg_sphinx_contrib_gen_node': 'y',
                    'pkg_zest_releaser': 'y',
                    'git_gitignore': 'f',
                    'buildout_buildout': 'f',
                    'buildout_bootstrap': 'f'}

        self.call_FUT(os.path.join(self.fs_templates, 'basic_namespace'),
                                     tpl_vars, output_dir=self.fs_tempdir)
        self.assertTrue(os.path.exists('%s/%s' % (self.fs_tempdir,
                                       'docs/LICENSE.txt')))
        configurator = DummyConfigurator(variables=tpl_vars)
        configurator.target_directory = self.fs_tempdir
        basic_namespace_post_render(configurator)
        self.assertFalse(os.path.exists('%s/%s' % (self.fs_tempdir,
                                        'docs/LICENSE.GPL')))

    def test_render_license_gpl(self):
        tpl_vars = {'pkg_license': 'GPL', 'gpl': 'y', 'pkg_ns': 'mytruc',
                    'pkg_keywords': 'Python', 'pkg_author_name': 'me',
                    'pkg_author_email': 'me@.tld', 'pkg_url': 'http://.tld',
                    'pkg_zipsafe': 'false', 'year': 2013, 'pkg_project': 'my',
                    'pkg_description': 'testing my templates',
                    'pkg_travis': 'y', 'pkg_nose': 'y', 'pkg_coverage': 'y',
                    'pkg_coveralls': 'y', 'dcvs_nick': 'jpcw',
                    'forgeurl': 'https://github.com', 'pkg_sphinx': 'y',
                    'pkg_sphinx_contrib_gen_node': 'y',
                    'pkg_zest_releaser': 'y',
                    'git_gitignore': 'f',
                    'buildout_buildout': 'f',
                    'buildout_bootstrap': 'f'
                    }

        self.call_FUT(os.path.join(self.fs_templates, 'basic_namespace'),
                                     tpl_vars, output_dir=self.fs_tempdir)
        self.assertTrue(os.path.exists('%s/%s' % (self.fs_tempdir,
                                       'docs/LICENSE.txt')))
        configurator = DummyConfigurator(variables=tpl_vars)
        configurator.target_directory = self.fs_tempdir
        self.assertTrue(os.path.exists('%s/%s' % (self.fs_tempdir,
                                       'docs/LICENSE.GPL')))


# vim:set et sts=4 ts=4 tw=80:
