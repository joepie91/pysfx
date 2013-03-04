#!/usr/bin/env python

"""
distutils/setuptools install script. See inline comments for packaging documentation.
"""

import os
import sys

try:
  from setuptools import setup
  # hush pyflakes
  setup
except ImportError:
  from distutils.core import setup

try:
  from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
  from distutils.command.build_py import build_py

packages = ['pysfx']

package_dir = {}

package_data = {}

scripts = [
  'script/pysfx'
]


setup(
  name='pysfx',
  version='0.1',
  maintainer='Sven Slootweg',
  maintainer_email='admin@cryto.net',
  description='Tool for creating self-extracting Python scripts with autorun.',
  url='http://www.cryto.net/projects/pysfx/',
  packages=packages,
  package_dir=package_dir,
  package_data=package_data,
  include_package_data=True,
  scripts=scripts,
  install_requires=['argparse'],
  cmdclass={'build_py': build_py}
)

