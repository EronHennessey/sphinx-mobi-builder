#!/usr/bin/env python
from setuptools import setup

long_desc = """
Sphinx .mobi builder, originally from Gist:
https://gist.github.com/kroger/5866756
"""

setup(name='sphinx-mobi-builder',
      description="""
        A Sphinx builder for .mobi (Kindle) files.""",
      version='0.2',
      install_requires=['docutils>=0.12', 'Sphinx>=1.0'],
      packages=['sphinx/builders'],
      author='Eron Hennessey, Pedro Kroger',
      author_email='eron@abstrys.com',
      url='https://github.com/EronHennessey/sphinx-mobi-builder',
      )

