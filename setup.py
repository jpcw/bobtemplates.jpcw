# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os


version = '0.1-dev'

here = os.path.abspath(os.path.dirname(__file__))

def read_file(*pathes):
    path = os.path.join(here, *pathes)
    if os.path.isfile(path):
        with open(path, 'r') as desc_file:
            return desc_file.read()
    else:
        return ''

desc_files = (('README.rst',), ('docs', 'CHANGES.rst'),
              ('docs', 'CONTRIBUTORS.rst'))

long_description = '\n\n'.join([read_file(*pathes) for pathes in desc_files])

install_requires=['setuptools', 'mr.bob']


setup(name='bobtemplates.jpcw',
      version=version,
      description="bobtemplates basic_namespace",
      long_description=long_description,
      platforms = ["any"],
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD",
        ],
      keywords='bobtemplates',
      author='Jean-Philippe Camguilhem',
      author_email='jp.camguilhem@gmail.com',
      url='https://github.com/jpcw/bobtemplates.jpcw',
      license='BSD',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['bobtemplates'],
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

# vim:set et sts=4 ts=4 tw=80:
