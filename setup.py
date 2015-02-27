#!/usr/bin/env python

from distutils.core import setup

install_requires = ['requests (==2.5.3)', 'httmock (==1.2.2)']

setup(name='zenoss-api',
      version='0.1',
      description='Zenoss JSON API Python Library',
      author='Efren Fuentes',
      packages=['zenoss_api'],
      requires=install_requires)
