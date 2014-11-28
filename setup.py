#!/usr/bin/env python
from distutils.core import setup

long_desc = """
Sphinx .mobi builder, originally from Gist:
https://gist.github.com/kroger/5866756
"""

setup(name='sphinx-mobi-builder',
      description="""
        A Sphinx builder for .mobi (Kindle) files.""",
      version='0.1',
      requires=['docutils'],
      packages=['sphinx/builders'],
      scripts=[],
      author='Pedro Kroger',
      author_email='eron@abstrys.com',
      url='https://gist.github.com/kroger/5866756',
      )
