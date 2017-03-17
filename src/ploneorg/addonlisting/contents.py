# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from plone.dexterity.content import Container
from plone.dexterity.content import Item
from ploneorg.addonlisting import _
from ploneorg.addonlisting import PYPI_URL
from ploneorg.addonlisting.interfaces import IAddOn
from ploneorg.addonlisting.interfaces import IAddOnFolder
from ploneorg.addonlisting.interfaces import ICategory
from ploneorg.addonlisting.interfaces import IMapping
from ploneorg.addonlisting.interfaces import IPyPIClassifierMapping
from ploneorg.addonlisting.interfaces import IVersionEggInfo
from ploneorg.addonlisting.interfaces import IVersionInfo
from z3c.form.object import registerFactoryAdapter
from zope.interface import implementer
from zope.interface import implements
from zope.interface import Interface
from zope.schema import Date
from zope.schema import TextLine


@implementer(IAddOnFolder)
class AddOnFolder(Container):
    implements(IAddOnFolder)


@implementer(IAddOn)
class AddOn(Item):
    implements(IAddOn)

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
    implements(IMapping)


registerFactoryAdapter(IMapping, Mapping)


@implementer(IPyPIClassifierMapping)
class PyPIClassifierMapping(Base):
    implements(IPyPIClassifierMapping)

    @property
    def version(self):
        return self.value

registerFactoryAdapter(IPyPIClassifierMapping, PyPIClassifierMapping)


@implementer(ICategory)
class Category(Base):
    implements(ICategory)

registerFactoryAdapter(ICategory, Category)


@implementer(IVersionInfo)
class VersionInfo(Base):
    implements(IVersionInfo)

registerFactoryAdapter(IVersionInfo, VersionInfo)


@implementer(IVersionEggInfo)
class VersionEggInfo(Base):
    implements(IVersionEggInfo)

registerFactoryAdapter(IVersionEggInfo, VersionEggInfo)
