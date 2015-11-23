=====================================================
Sphinxjp.themes.gopher
=====================================================

| tell-k
| https://github.com/tell-k/sphinxjp.themes.gopher

Title Slide
====================================

Heading1
====================================

Lorem ipsum dolor sit amet, consectetur adipisicing elit ...

Heading2
--------------------

Lorem ipsum dolor sit amet, consectetur adipisicing elit, ...

Heading3
~~~~~~~~~~~~~~~~~~~

Lorem ipsum dolor sit amet, consectetur adipisicing elit, ...

Heading4
++++++++++++++++

Lorem ipsum dolor sit amet, consectetur adipisicing elit, ...

Heading5
################

Lorem ipsum dolor sit amet, consectetur adipisicing elit, ...

Text Formatting
====================================

* ``*italic*`` => *italic*
* ``**bold**`` => **bold**
* ```python<www.python.org>`_`` => `python <www.python.org>`_
* ````verbatim```` => ``verbatim``

List and bullets
=================================

* This is a bulleted list.

  * Child1

* It has two items, the second
  item uses two lines. (note the indentation)

1. This is a numbered list.

  1. Child1

2. It has two items too.

Directive
=================================

This is a simple example::

 Lorem ipsum dolor sit amet, consectetur adipisicing elit, 
 sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
 Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
 nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
 reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
 Excepteur sint occaecat cupidatat non proident, 
 sunt in culpa qui officia deserunt mollit anim id est laborum.

Admonitions (Docutils origin)
==============================

.. danger::
   This is sample of admonition directive for "Danger".
   Lorem ipsum dolor sit amet, consectetur adipisicing elit ...
   Lorem ipsum dolor sit amet, consectetur adipisicing elit ...

.. error::
   This is sample of admonition directive for "Error".
   Lorem ipsum dolor sit amet, consectetur adipisicing elit ...
   Lorem ipsum dolor sit amet, consectetur adipisicing elit ...

.. warning::
   This is sample of admonition directive for "Warning".
   Lorem ipsum dolor sit amet, consectetur adipisicing elit ...
   Lorem ipsum dolor sit amet, consectetur adipisicing elit ...

.. caution::
   This is sample of admonition directive for "Caution".
   Lorem ipsum dolor sit amet, consectetur adipisicing elit ...
   Lorem ipsum dolor sit amet, consectetur adipisicing elit ...


Admonitions (Docutils origin)
==============================

.. attention:: This is sample of admonition directive for "Attention".
   Lorem ipsum dolor sit amet, consectetur adipisicing elit ...
   Lorem ipsum dolor sit amet, consectetur adipisicing elit ...

.. important:: This is sample of admonition directive for "Important".
   Lorem ipsum dolor sit amet, consectetur adipisicing elit ...
   Lorem ipsum dolor sit amet, consectetur adipisicing elit ...

.. note:: This is sample of admonition directive for "Note".
   Lorem ipsum dolor sit amet, consectetur adipisicing elit ...
   Lorem ipsum dolor sit amet, consectetur adipisicing elit ...

.. hint:: This is sample of admonition directive for "Hint".
   Lorem ipsum dolor sit amet, consectetur adipisicing elit ...
   Lorem ipsum dolor sit amet, consectetur adipisicing elit ...

Admonitions (Docutils origin)
==============================

.. tip::
   This is sample of admonition directive for "Tip".

Admonitions (Sphinx Additional)
===============================

.. seealso::
   This is sample of admonition directive for "SeeAlso".


.. versionadded:: 0.3.1
   Here is description of specification which added on that version.


.. versionchanged:: 0.8
   Here is description of specification which changed on that version.


.. deprecated:: 0.8
   Here is description of specification which changed on that version.


.. code-block:: python
   :linenos:

   >>> from fibo import fib, fib2
   >>> fib(500)
   1 1 2 3 5 8 13 21 34 55 89 144 233 377

.. todo:: TODO directive.


Footnotes
=========
I have footnoted a first item [#f1]_ and second item [#f2]_.
Lorem ipsum dolor sit amet [#f3]_ , consectetur adipisicing elit ...

---------

.. [#f1] My first footnote. My first footnote.My first footnote.My first footnote.My first footnote.My first footnote.
.. [#f2] My second footnote.
.. [#f3] A footnote contains body elements, consistently indented by at
   least 3 spaces.

Citation
========

Citation references, like [CIT2002]_.
Note that citations may get
rearranged, e.g., to the bottom of
the "page".

Citation labels contain alphanumerics,
underlines, hyphens and fullstops.
Case is not significant.

Given a citation like [this]_, one
can also refer to it like this_.

---------

.. [CIT2002] A citation
   (as often used in journals).
.. [this] here.

Table
======

+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | ...        | ...      |          |
+------------------------+------------+----------+----------+

Structural Elements
===================

Section Title
-------------

That's it, the text just above this line.

Transitions
-----------

Here's a transition:

---------

It divides the section.

Bullet Lists
=============

- A bullet list

  + Nested bullet list.
  + Nested item 2.

- Item 2.

  Paragraph 2 of item 2.

  * Nested bullet list.
  * Nested item 2.

    - Third level.
    - Item 2.

  * Nested item 3.

Enumerated Lists
==================

#. List items may also be auto-enumerated.
#. List items may also be auto-enumerated.
#. List items may also be auto-enumerated.
#. List items may also be auto-enumerated.
#. List items may also be auto-enumerated.
#. List items may also be auto-enumerated.
#. List items may also be auto-enumerated.


Definition Lists
==================

Term
    Definition
Term : classifier
    Definition paragraph 1.

    Definition paragraph 2.
Term
    Definition

Field Lists
=============

:what: Field lists map field names to field bodies, like database
       records.  They are often part of an extension syntax.  They are
       an unambiguous variant of RFC 2822 fields.

:how arg1 arg2:

    The field marker is a colon, the field name, and a colon.

    The field body may contain one or more body elements, indented
    relative to the field marker.

Option Lists
=============

-a            command-line option "a"
-b file       options can have arguments
              and long descriptions
--long        options can be long also
--input=file  long options can also have
              arguments

--very-long-option
              The description can also start on the next line.

              The description may contain multiple body elements,
              regardless of where it starts.

Option Lists
=============

-x, -y, -z    Multiple options are an "option group".
-v, --verbose  Commonly-seen: short & long options.
-1 file, --one=file, --two file
              Multiple options with arguments.
/V            DOS/VMS-style options too


Literal Blocks
==============

Literal blocks are indicated with a double-colon ("::") at the end of
the preceding paragraph (over there ``-->``).  They can be indented::

    if literal_block:
        text = 'is left as-is'
        spaces_and_linebreaks = 'are preserved'
        markup_processing = None

Or they can be quoted without indentation::

>> Great idea!
>
> Why didn't I think of that?

Line Blocks
==============

| This is a line block.  It ends with a blank line.
|     Each new line begins with a vertical bar ("|").
|     Line breaks and initial indents are preserved.
| Continuation lines are wrapped portions of long lines;
  they begin with a space in place of the vertical bar.
|     The left edge of a continuation line need not be aligned with
  the left edge of the text above it.

| This is a second line block.
|
| Blank lines are permitted internally, but they must begin with a "|".

Line Blocks
==============

Take it away, Eric the Orchestra Leader!

    | A one, two, a one two three four
    |
    | Half a bee, philosophically,
    |     must, *ipso facto*, half not be.
    | But half the bee has got to be,
    |     *vis a vis* its entity.  D'you see?
    |
    | But can a bee be said to be
    |     or not to be an entire bee,
    |         when half the bee is not a bee,
    |             due to some ancient injury?
    |
    | Singing...

Block Quotes
==============

Block quotes consist of indented body elements:

    My theory by A. Elk.  Brackets Miss, brackets.  This theory goes
    as follows and begins now.  All brontosauruses are thin at one
    end, much much thicker in the middle and then thin again at the
    far end.  That is my theory, it is mine, and belongs to me and I
    own it, and what it is too.

    -- Anne Elk (Miss)

Doctest Blocks
===============

>>> print 'Python-specific usage examples; begun with ">>>"'
Python-specific usage examples; begun with ">>>"
>>> print '(cut and pasted from interactive Python sessions)'
(cut and pasted from interactive Python sessions)

Topics
================================

.. topic:: Topic Title

   This is a topic.
   Lorem ipsum dolor sit amet, consectetur adipisicing elit, 
   sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
   Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
   nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
   reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
   Excepteur sint occaecat cupidatat non proident, 
   sunt in culpa qui officia deserunt mollit anim id est laborum.


Version Add
===================

.. versionadded:: 2.5
   The *spam* parameter.

.. versionchanged:: 2.5
   The *spam* parameter.

.. deprecated:: 2.5
   The *spam* parameter.

.. rubric:: Footnotes

.. centered:: LICENSE AGREEMENT

.. hlist::
   :columns: 3

   * A list of
   * short items
   * that should be
   * displayed
   * horizontally

Compound Paragraph
===================

.. compound::

   This paragraph contains a literal block::

       Connecting... OK
       Transmitting data... OK
       Disconnecting... OK
      
   and thus consists of a simple paragraph, a literal block, and
   another simple paragraph.  Nonetheless it is semantically *one*
   paragraph.

This construct is called a *compound paragraph* and can be produced
with the "compound" directive.

Glossary
=========

.. glossary::

   environment
      A structure where information about all documents under the root is
      saved, and used for cross-referencing.  The environment is pickled
      after the parsing stage, so that successive runs only need to read
      and parse new and changed documents.

   source directory
      The directory which, including its subdirectories, contains all
      source files for one Sphinx project.


Productionlist
===============================

.. productionlist::
   try_stmt: try1_stmt | try2_stmt
   try1_stmt: "try" ":" `suite`
            : ("except" [`expression` ["," `target`]] ":" `suite`)+
            : ["else" ":" `suite`]
            : ["finally" ":" `suite`]
   try2_stmt: "try" ":" `suite`
            : "finally" ":" `suite`
