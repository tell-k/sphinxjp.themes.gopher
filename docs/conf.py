# -*- coding: utf-8 -*-
#
# -- General configuration ----------------------------------------

source_suffix = '.rst'
master_doc = 'index'

project = u'sphinx theme for Go talk style presentation.'
copyright = u'2018, tell-k'

version = '0.2.1'

# -- Options for HTML output --------------------------------------

extensions = ['sphinxjp.themes.gopher', 'sphinx.ext.todo']
html_theme = 'gopher'
html_theme_options  = {
   'canonical': 'https://sphinxjpthemesgopher.readthedocs.io',

   'ogp_title':'sphinxjp.themes.gopher',
   'ogp_image':'https://raw.githubusercontent.com/tell-k/sphinxjp.themes.gopher/master/docs/_static/img/ogp.png',
   'ogp_description':'A sphinx theme for generate gotalk style presentation. #sphinxjp',

   'og_url':'https://sphinxjpthemesgopher.readthedocs.io',
   'og_site_name':'readthedocs',
   'og_type':'article',
   'og_author':'https://github.com/tell-k',

   'twitter_card_type':'summary_large_image',
   'twitter_card_creator':'@tell_k',

   'note_enabled': True,
}
html_use_index = False

html_static_path = ['_static']
todo_include_todos = True
