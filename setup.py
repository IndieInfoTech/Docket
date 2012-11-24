#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

from docket import __version__

with open('README.md') as stream:
  long_desc = stream.read()

setup(
    name='docket',
    version=__version__,
    author='Shane R. Spencer',
    author_email='shane@bogomip.com',
    packages=['docket'],
    url='https://github.com/IndieInfoTech/Docket',
    license='MIT',
    description='Information Docket System',
    long_description=long_desc,
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Development Status :: 1 - Planning',
        'Environment :: No Input/Output (Daemon)',
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Topic :: System :: Networking',
        'Topic :: Database',
        'Topic :: Communications',
        'Topic :: System :: Distributed Computing',
    ],
)


