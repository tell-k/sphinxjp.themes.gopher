# -*- coding: utf-8 -*-
#
# -- General configuration ----------------------------------------

source_suffix = '.rst'
master_doc = 'index'

project = u'sphinx theme for Go talk style presentation.'
copyright = u'2015, tell-k'

version = '0.1.1'

# -- Options for HTML output --------------------------------------

extensions = ['sphinxjp.themes.gopher', 'sphinx.ext.todo']
html_theme = 'gopher'
html_use_index = False

# html_static_path = ['_static']
todo_include_todos = True
