# -*- coding: utf-8 -*-
import os
import re

from setuptools import setup, find_packages


here = os.path.dirname(__file__)
version_regex = re.compile(r".*__version__ = '(.*?)'", re.S)
version_script = os.path.join(here, 'src', 'sphinxjp',
                              'themes', 'gopher', '__init__.py')
version = version_regex.match(open(version_script, 'r').read()).group(1)


install_requires = [
    'Sphinx',
]

setup_requires = [
    "pytest-runner"
]

tests_require = [
    'pytest-cov',
    'pytest',
    'mock',
]

long_description = '\n'.join([
    open(os.path.join(here, "README.rst")).read(),
    open(os.path.join(here, "src", "AUTHORS.txt")).read(),
    open(os.path.join(here, "src", "HISTORY.txt")).read(),
])

classifiers = [
    "Development Status :: 4 - Beta",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Framework :: Sphinx",
    "Framework :: Sphinx :: Extension",
    "Framework :: Sphinx :: Theme",
    "Topic :: Software Development",
    "Topic :: Software Development :: Documentation",
    "Topic :: Text Processing :: Markup",
]

description = 'A sphinx theme for generate gotalk style presentation. #sphinxjp'  # NOQA

setup(
    name='sphinxjp.themes.gopher',
    version=version,
    description=description,
    long_description=long_description,
    classifiers=classifiers,
    keywords=['sphinx', 'reStructuredText', 'theme', 'presentation'],
    author='tell-k',
    author_email='ffk2005@gmail.com',
    url='https://github.com/tell-k/sphinxjp.themes.gopher',
    license='MIT',
    namespace_packages=['sphinxjp', 'sphinxjp.themes'],
    packages=find_packages('src', exclude=['tests']),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    entry_points= {
        'sphinx.html_themes': [
            'gopher = sphinxjp.themes.gohper',
        ]
    },
    zip_safe=False
)
