# -*- coding: utf-8 -*-
import os

import shlex

from setuptools import find_packages
from setuptools import setup
from setuptools.command.install import install
from setuptools import Command

import subprocess

from subprocess import check_call

class PostInstallCommand(install):

    def run(self):
        install.run(self)
        check_call("systemctl daemon-reload".split())
        check_call("systemctl enable intelcollector".split())

base_dir = os.path.dirname(__file__)
setup(
    name='IntelCollector',
    version='0.0.1',
    description='Collects and Transforms Intel From Various Sources',
    author='Japneet Chahal',
    setup_requires='setuptools',
    license='Copyright 2014 Yelp',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': ['intelcollector=collector.collector:main']},
    packages=find_packages(),
    include_package_data=True,
    data_files=[
        ('/usr/local/etc', ['config/intelCollectorConfig.yaml']),
        ('/usr/local/etc', ['config/url_list.yaml']),        
        ('/etc/systemd/system', ['config/intelcollector.service'])
    ],
    cmdclass={
        'install': PostInstallCommand
    }
)
