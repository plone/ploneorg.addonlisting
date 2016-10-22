.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
ploneorg.addonlisting
==============================================================================

Creates add-on listings for Plone.org in a visually appealing
way. Allow highlighting of curated add-ons, simpler/cleaner
descriptions of add-ons, and automated retrieval of data from
pypi.python.org.



Features
--------

- queries pypi.python.org for packages for a specifiable framework (default: Plone)

- lets you manually add packages

- with manually added packages, you can optionally specify just the
  package name and load the rest of the field values from PyPi

- lets you indicate which packages not to display in the listing

- lets you map PyPi classifiers and Python versions to friendlier
  display values

- lets you specify add-on categories that are used to organize the
  display of add-ons

- lets you indicate if an add-on should be highlighted ("curated")

- if an add-on has been marked as curated, you can override the
  summary and description

- lets you indicate which category an add-on belongs to

- displays the raw PyPi data (read-only)


Examples
--------

This add-on can be seen in action at the following sites:
- plone.org/addons


Documentation
-------------

Full documentation for end users can be found in the "docs" folder


Translations
------------

This product has been translated into

- English

- German


Installation
------------

Install ploneorg.addonlisting by adding it to your buildout::

    [buildout]

    ...

    eggs =
        ploneorg.addonlisting


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/plone/ploneorg.addonlisting/issues
- Source Code: https://github.com/plone/ploneorg.addonlisting



Support
-------

If you are having issues, please let us know via the issue tracker at
https://github.com/plone/ploneorg.addonlisting/issues



License
-------

The project is licensed under the GPLv2.
