# -*- coding: UTF-8 -*-
"""
@Summary : 
@Author  : Rey
@Time    : 2020-06-08 17:09
@Log     :
           author datetime(DESC) summary
"""

import io
from setuptools import find_packages, setup

VERSION = "1.0.3"

with io.open("README.md", 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='dx_tools',
    version=VERSION,
    description='tools',
    author='Rey',
    author_email='czp_fist@163.com',
    url='https://github.com/reydx/dx_tools',
    long_description=long_description,
    long_description_content_type='text/markdown',
    #packages=find_packages(),
    packages=['dx_tools'],
    #install_requires=['requests'],
)