#!/usr/bin/env python3

import sys, requests
from setuptools import setup, find_packages

setup(
    name='themekit-cli',
    version=open('./version').read(),
    author='Max Bridgland',
    author_email='mabridgland@protonmail.com',
    description='ThemeKit Helper On The Command Line',
    long_description=open('./README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ThemeKitApp/themekit-helper',
    packages=find_packages(),
    install_requires=[
        'colorama',
        'requests',
        'terminaltables'
    ],
    project_urls={
        'Wiki': 'https://github.com/ThemeKitApp/themekit-helper',
    },
    license='GNU General Public License v3 (GPLv3) (GPL)',
    zip_safe=True,
    entry_points={
        'console_scripts':[
            'themekitcli = themekitcli.__main__:main',
            'tkcli = themekitcli.__main__:main',
        ],
    },
    classifiers=[  # Used by PyPI to classify the project and make it searchable
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',

        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: IronPython',
        'Programming Language :: Python :: Implementation :: Jython',

        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',

        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Systems Administration',
        'Topic :: System :: Networking',
        'Topic :: Utilities',
    ]
)
