# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from plone.dexterity.content import Container
from plone.dexterity.content import Item
from plone.directives import form
from ploneorg.addonlisting import PYPI_URL
from ploneorg.addonlisting.interfaces import IAddOn
from ploneorg.addonlisting.interfaces import IAddOnFolder
from ploneorg.addonlisting.interfaces import ICategory
from ploneorg.addonlisting.interfaces import IFilterForm
from ploneorg.addonlisting.interfaces import IMapping
from ploneorg.addonlisting.interfaces import IPyPIClassifierMapping
from ploneorg.addonlisting.interfaces import IVersionEggInfo
from ploneorg.addonlisting.interfaces import IVersionInfo
from z3c.form import button
from z3c.form.object import registerFactoryAdapter
from zope.interface import implementer


@implementer(IAddOnFolder)
class AddOnFolder(Container):
    pass


@implementer(IAddOn)
class AddOn(Item):

    @property
    def package_link(self):
        return PYPI_URL + '/' + self.title

    @property
    def dict(self):
        return self.__dict__


class Base(object):

    def __getitem__(self, key):
        return getattr(self, key, None)

    def __setitem__(self, key, value):
        setattr(self, key, value)


@implementer(IMapping)
class Mapping(Base):
    pass


registerFactoryAdapter(IMapping, Mapping)


@implementer(IPyPIClassifierMapping)
class PyPIClassifierMapping(Base):

    @property
    def version(self):
        return self.value


registerFactoryAdapter(IPyPIClassifierMapping, PyPIClassifierMapping)


@implementer(ICategory)
class Category(Base):
    pass


registerFactoryAdapter(ICategory, Category)


@implementer(IVersionInfo)
class VersionInfo(Base):
    pass


registerFactoryAdapter(IVersionInfo, VersionInfo)


@implementer(IVersionEggInfo)
class VersionEggInfo(Base):
    pass


registerFactoryAdapter(IVersionEggInfo, VersionEggInfo)


class FilterForm(form.SchemaForm):

    schema = IFilterForm
    ignoreContext = True
    label = u'Filter'
    description = u'Filter after certain criteria.'

    @button.buttonAndHandler(u'Ok')
    def handleApply(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        print data
        # Do something with valid data here

        # Set status on this form page
        # (this status message is not bind to the session
        #  and does not go thru redirects)
        self.status = 'Thank you very much!'

    @button.buttonAndHandler(u'Cancel')
    def handleCancel(self, action):
        """User cancelled. Redirect back to the front page.
        """
        self.status = 'Canceled!'
