###################
sphinx-mobi-builder
###################

A Sphinx builder for .mobi (Kindle) files.

This script was originally from GitHub Gist `#5866756`__, by Pedro Kroger.

.. __: https://gist.github.com/kroger/5866756

Important: Why you *don't* want to use this!
============================================

In my humble opionion, the *best way* to generate ``.mobi`` files from Sphinx is:

#. Turn *off* ``smartquotes`` in your ``conf.py``. This is important to keep quote characters that
   work *just fine* with the Epub format from being rendered incorrectly after conversion by
   ``kindlegen``::

       smartquotes = False

#. Generate an Epub, by running::

      sphinx-build -b epub <sourcedir> <outputdir>

#. Run kindlegen_ to convert the Epub to a ``.mobi``::

      kindlegen <outputdir>/<title>.epub -o <title>.mobi

   You can script this easily by just adding this line to your ``Makefile`` when building, for
   example.

**That's it!** All you really need to do is follow Sphinx's recommendations regarding building Epub
files here:

* http://www.sphinx-doc.org/en/master/faq.html#epub-faq

That's how *I'm* building ``.mobi`` files these days.

Legacy instructions
===================

OK, if you really want to use this, here are some tips... the *Legacy install instructions!*

Requirements
------------

The ``.mobi`` builder requires:

* kindlegen_ - A command-line Kindle builder from Amazon.com. Just download the application and put it in your
  *PATH*.


Installation
------------

To install the script, download the source and run ``setup.py install``. It will be copied into your
Python ``site-packages`` directory.


Using the builder with Sphinx
-----------------------------

To use the builder with Sphinx, add ``sphinx.builders.mobi`` to your *extensions* in ``conf.py``::

    extensions = [
       # other extensions... ,
       'sphinx.builders.mobi'
       ]

Configuring the builder
-----------------------

The following configuration values can be used in ``conf.py``. At a minimum, you must set the *mobi_theme* option:

mobi_add_visible_links
    Whether or not to write out the full text of a hyperlink next to the link itself. If the
    document will be read on paper (or printed), it is a good idea to set this to ``True``.

    **Default**: ``True``

mobi_author
    The author of the book.

    **Default**: ``'unknown'``

mobi_basename
    The basename of the output file (the part of the filename that precedes ``.mobi``)

    **Default**: The project name, with spaces removed.

mobi_copyright
    The copyright holder of the book.

    **Default**: The value of **copyright** in ``conf.py``

mobi_cover
    The cover image for the book. This should be in ``.jpg`` format.

    **Default**: No cover image is used.

mobi_exclude_files
    TBD

    **Default**: no files are excluded.

mobi_identifier
    TBD

    **Default**: ``'unknown'``

mobi_language
    TBD

    **Default**: The value of *language* in ``conf.py``, or ``'en'`` if *language* is not set.

mobi_post_files
    TBD

    **Default**: no post files are used.

mobi_pre_files
    TBD

    **Default**: no pre files are used.

mobi_publisher
    The publisher name for the book.

    **Default**: ``'unknown'``

mobi_scheme
    TBD

    **Default**: ``'unknown'``

mobi_theme
    *Required*. The mobi theme-file to use. If you don't have a theme of your own, I suggest using
    the ``epub`` theme::

        mobi_theme = 'epub'

mobi_title
    TBD

    **Default**: The value of *html_title* in ``conf.py``.

mobi_tocdepth
    TBD

    **Default**: ``3``.

mobi_tocdup
    TBD

    **Default**: ``True``

mobi_uid
    TBD

    **Default**: ``'unknown'``

License
=======

As per the original script, this code is made available using the `BSD Open Source license`__.

.. __: http://opensource.org/licenses/BSD-3-Clause

.. _kindlegen: http://www.amazon.com/gp/feature.html?docId=1000765211
