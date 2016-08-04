Concept of ploneorg.addonlisting (SW-Design and Implementation)
===============================================================

ploneorg.addonlisting is a separate package from ploneorg.core, where some other content types and functionality for the plone.org Webpage are developed.
This is done with the intention to reuse this functionality.

Plone Add'ons that could an should be presented to users should be released and life on PyPI (Python Package Index).
Therefore we could use PyPI package lookup to get all Plone Add'ons via a filter on relevant PyPI classifiers.

PyPI-Classifiers
----------------

All Plone related Package should be tagged with the PyPI-Classifier

* Framework :: Plone

All Add'ons should have been tagged additionally with the PyPI-Classifier:

* Environment :: Plugins   *(Proposal)*

additional classifiers that reflects the compatible Plone Version:

* Framework :: Plone :: 3.2
* Framework :: Plone :: 3.3
* Framework :: Plone :: 4.0
* Framework :: Plone :: 4.1
* Framework :: Plone :: 4.2
* Framework :: Plone :: 4.3
* Framework :: Plone :: 5.0

Also if possible following classifiers which reflects Python compatibility should read

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

Plone Packages should also indicate which status the current package has:

* Development Status :: 1 - Planning
* Development Status :: 2 - Pre-Alpha
* Development Status :: 3 - Alpha
* Development Status :: 4 - Beta
* Development Status :: 5 - Production/Stable
* Development Status :: 6 - Mature
* Development Status :: 7 - Inactive

Storage
-------

External lookups on runtime should be considered harmful, so we should frequently update (CRON) the Listing and store the data in Plone itself.
Plone has a fantastic Content Type story, so we use a Plone Dexterity Content Type for storing the data.

AddOn
^^^^^

We will decide between two types of Add'ons we want to show on plone.org:

* Curated Add'ons
* Add'ons

Additionally we do have PyPI Packages that are tagged with the classifiers but should not show up (core packages, unmaintained, harmful, ...).

Fields
``````

* Name (PyPI Name)
* Tag-Line (Text / TextLine for a one sentence description used in isotope)
* Description (RichText, Marketing Text for curated add'ons)
* Lead Image (Used in Listings and Isotope)
* Tags (Keywords)
* Curated (Bool)
* Blacklist (Bool, for Core and harmful packages)
* Unmaintained (For highlighting Old Packages that may still be known but shoud not be used anymore) - maybe replaced_by should be added.
* Download Numbers
* Links (PyPI, Bugfix/Issue-Tracker, Docs)
* Plone Version Support

AddOnFolder
^^^^^^^^^^^


Storage-Details
---------------

As we would like to store the data in Plone for easier access and view, we should prevent that users edit fields that are auto-updated.
For implementation we use Plone Dexterity XML Schemas, there you could use form:mode (http://docs.plone.org/external/plone.app.dexterity/docs/reference/dexterity-xml.html#mode) for hide or view mode.
Additionally we might should consider showing those data in edit mode, but as mode view not input and group them in a different tab-group (Fieldset).
