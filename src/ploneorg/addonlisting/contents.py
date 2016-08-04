# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from ploneorg.addonlisting import _
from ploneorg.addonlisting.interfaces import IAddOnFolder
from ploneorg.addonlisting.interfaces import IAddOn
from plone.dexterity.content import Item
from plone.dexterity.content import Container
from zope.interface import implements


class AddOnFolder(Container):
    implements(IAddOnFolder)


class AddOn(Item):
    implements(IAddOn)
