# -*- coding: utf-8 -*-
#
# -- General configuration ----------------------------------------

source_suffix = '.rst'
master_doc = 'index'

project = u'sphinx theme for Go talk style presentation.'
copyright = u'2018, tell-k'

version = '0.1.1'

# -- Options for HTML output --------------------------------------

extensions = ['sphinxjp.themes.gopher', 'sphinx.ext.todo']
html_theme = 'gopher'
html_theme_options  = {
   'ogp_title':'sphinxjp.themes.gopher',
   'ogp_image':'https://pythonhosted.org/sphinxjp.themes.gopher/_static/img/ogp.png',
   'ogp_description':'A sphinx theme for generate gotalk style presentation. #sphinxjp',

   'og_url':'https://pythonhosted.org/sphinxjp.themes.gopher/',
   'og_site_name':'pthonhosted',
   'og_type':'article',
   'og_author':'https://github.com/tell-k',

   'twitter_card_type':'summary_large_image',
   'twitter_card_creator':'@tell_k',
}
html_use_index = False

html_static_path = ['_static']
todo_include_todos = True
