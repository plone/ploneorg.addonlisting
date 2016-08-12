# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from ploneorg.addonlisting import _
from ploneorg.addonlisting.interfaces import IAddOnFolder
from ploneorg.addonlisting.interfaces import IAddOn
from ploneorg.addonlisting.interfaces import IMapping
from ploneorg.addonlisting.interfaces import IVersionInfo
from plone.dexterity.content import Item
from plone.dexterity.content import Container
from zope.schema import Date
from zope.schema import TextLine
from zope.interface import implements
from zope.interface import Interface
from z3c.form.object import registerFactoryAdapter


class AddOnFolder(Container):
    implements(IAddOnFolder)


class AddOn(Item):
    implements(IAddOn)


class Mapping(object):
    implements(IMapping)

    def __init__(self):
        pass


registerFactoryAdapter(IMapping, Mapping)


class VersionInfo(object):
    implements(IVersionInfo)

    def __init__(self):
        pass


registerFactoryAdapter(IVersionInfo, VersionInfo)
