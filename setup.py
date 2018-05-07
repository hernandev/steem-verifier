#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

# meta.
NAME = 'steem-verifier'
DESCRIPTION = 'Easy verification of Steem transaction signatures.'
URL = 'https://github.com/hernandev/verifier'
EMAIL = 'diego@hernandev.com'
AUTHOR = 'Diego Hernandes'

# dist dependencies.
REQUIRED = [
    'steem'
]

# build dependencies.
BUILD_REQUIRED = [
    'twine',
    'wheel',
    'setuptools'
]
# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that!

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.rst' is present in your MANIFEST.in file!
# with io.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
#     long_description = '\n' + f.read()


class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPi via Twine…')
        os.system('twine upload dist/*')

        sys.exit()


# Where the magic happens:
setup(
    name=NAME,
    version='1.0.0',
    description=DESCRIPTION,
    keywords=['steem', 'blockchain', 'signature', 'transaction'],
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(exclude=('scripts')),
    entry_points={
            'console_scripts': [
                'steem-verifier=verifier.cli:entry'
            ],
    },
    install_requires=REQUIRED,
    extras_require={
        'dev': BUILD_REQUIRED,
        'build': BUILD_REQUIRED
    },
    include_package_data=True,
    license='MIT',

    classifiers=[
            # Trove classifiers
            # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English', 'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Development Status :: 4 - Beta'
    ],
    # $ setup.py publish support.
    cmdclass={
        'upload': UploadCommand
    },
)