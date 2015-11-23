Go talks style presentation theme for Sphinx.

|travis| |coveralls| |downloads| |version| |license| |requires|


Output Sample
=============
:output: http://packages.python.org/sphinxjp.themes.gopher/
:source: http://packages.python.org/sphinxjp.themes.gopher/_sources/index.txt


Features
========
* Provide `Go talks <http://talks.golang.org/>`_ style theme for render presetation.
* You don't need to learn a special directive and role. All you have to know generally ReStructuredText.
* Support PDF export.

PDF Export
============

Presentations can be exported to PDF via a print stylesheet. This feature requires that you use Google Chrome or Chromium. 

1. Open your presentation.
2. Open the in-browser print dialog (CMD+P).
3. Change the Destination setting to Save as PDF.
4. Click Save.

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

.. |downloads| image:: https://img.shields.io/pypi/dm/sphinxjp.themes.gopher.svg
    :target: http://pypi.python.org/pypi/sphinxjp.themes.gopher/
    :alt: downloads

.. |version| image:: https://img.shields.io/pypi/v/sphinxjp.themes.gopher.svg
    :target: http://pypi.python.org/pypi/sphinxjp.themes.gopher/
    :alt: latest version

.. |license| image:: https://img.shields.io/pypi/l/sphinxjp.themes.gopher.svg
    :target: http://pypi.python.org/pypi/sphinxjp.themes.gopher/
    :alt: license
