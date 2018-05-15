#!/usr/bin/env python

from distutils.core import setup

setup(
    name='ragnar',
    version='0.1',
    description='Linaro kernel build and bisect tool',
    author='Dan Rue',
    author_email='dan.rue@linaro.org',
    #url='',
    packages=['ragnar'],
    entry_points={
        'console_scripts': [
            'ragnar=ragnar.cli:main'
        ]
    },
)
