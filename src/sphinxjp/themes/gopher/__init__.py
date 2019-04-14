# -*- coding: utf-8 -*-
"""
    sphinxjp.themes.gopher
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :author: tell-k <ffk2005@gmail.com>
    :copyright: tell-k. All Rights Reserved.
"""
from os import path

package_dir = path.abspath(path.dirname(__file__))
template_path = path.join(package_dir, 'templates', 'gopher')

__version__ = '0.2.3'


def get_path():
    """entry-point for theme."""
    return template_path


def setup(app):
    """entry-point for sphinx directive."""
    app.add_html_theme('gopher', get_path())
