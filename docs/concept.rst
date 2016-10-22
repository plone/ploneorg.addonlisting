Concept of ploneorg.addonlisting (SW-Design and Implementation)
===============================================================

ploneorg.addonlisting is a separate package from ploneorg.core, which includes content types and functionality for the Plone.org site.

Plone add-ons should continue to be released to PyPI (pypi.python.org, the Python Package Index).
ploneorg.addonlisting reads PyPI to get information on all Plone add-ons, applying a filter on relevant PyPI classifiers, but also lets us manually indicate which add-ons to hide, which to highlight ("curate"), and, for curated add-ons, override the summary and description of the add-on.

PyPI-Classifiers
----------------

All Plone related add-ons should be tagged with the PyPI classifier

* Framework :: Plone

All add-ons should have been tagged additionally with the PyPI classifier:

* Environment :: Plugins   *(Proposal)*

Additional classifiers that reflect the compatible Plone version:

* Framework :: Plone :: 3.2
* Framework :: Plone :: 3.3
* Framework :: Plone :: 4.0
* Framework :: Plone :: 4.1
* Framework :: Plone :: 4.2
* Framework :: Plone :: 4.3
* Framework :: Plone :: 5.0

Also, if possible, the following classifiers should be included to reflect the add-ons' Python version compatibility:

* Programming Language :: Python
* Programming Language :: Python :: 2
* Programming Language :: Python :: 2.3
* Programming Language :: Python :: 2.4
* Programming Language :: Python :: 2.5
* Programming Language :: Python :: 2.6
* Programming Language :: Python :: 2.7
* Programming Language :: Python :: 2 :: Only
* Programming Language :: Python :: 3
* Programming Language :: Python :: 3.0
* Programming Language :: Python :: 3.1
* Programming Language :: Python :: 3.2
* Programming Language :: Python :: 3.3
* Programming Language :: Python :: 3.4
* Programming Language :: Python :: 3.5
* Programming Language :: Python :: 3.6
* Programming Language :: Python :: 3 :: Only

Plone add-ons should also indicate their status:

* Development Status :: 1 - Planning
* Development Status :: 2 - Pre-Alpha
* Development Status :: 3 - Alpha
* Development Status :: 4 - Beta
* Development Status :: 5 - Production/Stable
* Development Status :: 6 - Mature
* Development Status :: 7 - Inactive

Storage
-------

Real-time queries to PyPi could be problematic, so we use a scheduled task (or "cron" job) to retrieve the add-on listing data from PyPi and we store the data locally in Plone.

We use a Plone Dexterity content type to store the add-on data locally.

Add-on
^^^^^^

There are two types of add-ons we want to show on Plone.org:

* Curated ("highlighted") add-ons
* add-ons

There are many Plone packages on PyPi that are tagged with the Plone classifiers but should not show up in the Plone.org add-on listing (e.g., core packages, unmaintained or harmful add-ons).

Fields
``````

* Name (PyPI package name)
* Tag-Line (Text / TextLine for a one sentence description used in isotope)
* Description (RichText, marketing text for curated add-ons)
* Lead Image (used in listings and isotope)
* Tags (keywords)
* Curated (boolean yes/no)
* Blacklist (boolean yes/no, for core and harmful add-ons)
* Unmaintained (for highlighting old add-ons that should no longer be used) [maybe we should add a replaced_by boolean?]
* Download count
* Links (e.g., to PyPI, issue tracker, documentation, project site)
* Plone version support

AddOnFolder
^^^^^^^^^^^


Storage Details
---------------

Since we store data locally in Plone for easier and faster access, we prevent users from editing field values that are auto-updated from PyPi.
 We use Plone Dexterity XML schemas, and the form:mode (http://docs.plone.org/external/plone.app.dexterity/docs/reference/dexterity-xml.html#mode) feature to hide or show fields.
Additionally we could show those data in edit mode but view only (not editable) and group them in a different tab group or fieldset.
