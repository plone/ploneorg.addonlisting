# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from ploneorg.addonlisting import _
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IPloneorgAddonlistingLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IAddOnFolder(Interface):
    """
    Content Type for Add'ons-Folder.
    """
    #form.model("models/addonfolder.xml")


class IAddOn(Interface):
    """
    Content Type for Add'ons.
    """
    #form.model("models/addon.xml")
