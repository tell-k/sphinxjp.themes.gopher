Go talks style presentation theme for Sphinx.

|travis| |coveralls| |version| |license| |requires|


Output Sample
=============
:output: https://sphinxjpthemesgopher.readthedocs.io
:source: https://sphinxjpthemesgopher.readthedocs.io/_sources/index.rst.txt


Features
========
* Provide `Go talks <http://talks.golang.org/>`_ style theme for render presetation.
* You don't need to learn a special directive and role. All you have to know generally ReStructuredText.
* Support PDF export.
* Support Presenter notes.
* Support OGP tags.

PDF Export
============

Presentations can be exported to PDF via a print stylesheet. This feature requires that you use Google Chrome or Chromium.

1. Open your presentation.
2. Open the in-browser print dialog (CMD+P).
3. Change the Destination setting to Save as PDF.
4. Click Save.

Presenter Notes
==================

１. Embed notes

.. code-block:: rst

 .. rst-class:: presenter-notes

   Lorem ipsum dolor sit amet, consectetur adipisicing elit,
   sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.


２. Turn on ``note_enabled`` in conf.py

.. code-block:: python

 html_theme_options  = {
    'note_enabled': True, # => default False.
 }

This will allow you to open a second window by pressing 'N' from your browser displaying your slides.
The second window is completely synced with your main window,
except that presenter notes are only visible on the second window.


.. image:: https://raw.githubusercontent.com/tell-k/sphinxjp.themes.gopher/master/docs/_static/img/presenter-notes.png
   :width: 70%

OGP Tags
===========

You can add OGP settings in conf.py.

.. code-block:: python

  html_theme_options  = {
      # for canonical
      'canonical':'https://sphinxjpthemesgopher.readthedocs.io',

      # for title and "og:title" and "twitter:title"
      'ogp_title':'Sphinxjp.themes.gopher',

      # for "og:image" and "twitter:image"
      'ogp_image':'https://sphinxjpthemesgopher.readthedocs.io/_static/img/ogp.png',

      # for description and "og:description" and "twitter:description"
      'ogp_description':'A sphinx theme for generate gotalk style presentation. #sphinxjp',

      # for "og:url"
      'og_url':'https://sphinxjpthemesgopher.readthedocs.io',

      # for "og:site_name"
      'og_site_name':'readthedocs',

      # for "og:type"
      'og_type':'article',

      # for "article:author"
      'og_author':'https://github.com/tell-k',

      # for "twitter:card". default "summary"
      'twitter_card_type':'summary_large_image',

      # for "twitter:site"
      'twitter_card_site':'@tell_k',

      # for "twitter:creator"
      'twitter_card_creator':'@tell_k',
  }

Caution
========
* It does not support the hosting of the http://talks.golang.org.
* It cannot enable to playground.

Set up
======
Make environment with pip::

    $ pip install sphinxjp.themes.gopher

Convert Usage
=============
setup conf.py with::

    extensions = ['sphinxjp.themes.gopher']
    html_theme = 'gopher'
    html_use_index = False

and run::

    $ make html

Requirement
=============
* Python 2.7 or later
* Sphinx 1.3.x or later.

Using
=============

* static files in `golang/tools <https://github.com/golang/tools/tree/master/cmd/present/static>`_

License
=======

* sphinxjp.themes.gopher Licensed under the `MIT license <http://www.opensource.org/licenses/mit-license.php>`_ .
* `orginal static files(styles.css, slides.js) are licensed under the BSD lincense <https://github.com/golang/tools/blob/master/LICENSE>`_

See the src/LICENSE.txt file for specific terms.

.. |travis| image:: https://travis-ci.org/tell-k/sphinxjp.themes.gopher.svg?branch=master
    :target: https://travis-ci.org/tell-k/sphinxjp.themes.gopher

.. |coveralls| image:: https://coveralls.io/repos/tell-k/sphinxjp.themes.gopher/badge.png
    :target: https://coveralls.io/r/tell-k/sphinxjp.themes.gopher/
    :alt: coveralls.io

.. |requires| image:: https://requires.io/github/tell-k/sphinxjp.themes.gopher/requirements.svg?branch=master
    :target: https://requires.io/github/tell-k/sphinxjp.themes.gopher/requirements/?branch=master
    :alt: requires.io

.. |version| image:: https://img.shields.io/pypi/v/sphinxjp.themes.gopher.svg
    :target: http://pypi.python.org/pypi/sphinxjp.themes.gopher/
    :alt: latest version

.. |license| image:: https://img.shields.io/pypi/l/sphinxjp.themes.gopher.svg
    :target: http://pypi.python.org/pypi/sphinxjp.themes.gopher/
    :alt: license
