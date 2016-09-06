# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from ploneorg.addonlisting import _
from ploneorg.addonlisting import PYPI_URL
from ploneorg.addonlisting.interfaces import IAddOnFolder
from ploneorg.addonlisting.interfaces import IAddOn
from ploneorg.addonlisting.interfaces import IMapping
from ploneorg.addonlisting.interfaces import IPyPIClassifierMapping
from ploneorg.addonlisting.interfaces import IVersionInfo
from ploneorg.addonlisting.interfaces import IVersionEggInfo
from plone.dexterity.content import Item
from plone.dexterity.content import Container
from zope.schema import Date
from zope.schema import TextLine
from zope.interface import implementer
from zope.interface import implements
from zope.interface import Interface
from z3c.form.object import registerFactoryAdapter


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


@implementer(IMapping)
class Mapping(object):
    implements(IMapping)

registerFactoryAdapter(IMapping, Mapping)


@implementer(IPyPIClassifierMapping)
class PyPIClassifierMapping(object):
    implements(IPyPIClassifierMapping)

    @property
    def version(self):
        return self.value

    def __getitem__(self, key):
        if key == 'key':
            return self.key
        elif key == 'value':
            return self.value

    def __setitem__(self, key, value):
        if key == 'key':
            self.key = value
        elif key == 'value':
            self.value = value

registerFactoryAdapter(IPyPIClassifierMapping, PyPIClassifierMapping)


@implementer(IVersionInfo)
class VersionInfo(object):
    implements(IVersionInfo)

registerFactoryAdapter(IVersionInfo, VersionInfo)


@implementer(IVersionEggInfo)
class VersionEggInfo(object):
    implements(IVersionEggInfo)

    def __getitem__(self, key):
        return getattr(self, key)

registerFactoryAdapter(IVersionEggInfo, VersionEggInfo)
