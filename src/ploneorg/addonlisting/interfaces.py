# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from ploneorg.addonlisting import _
from plone.supermodel import model
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IPloneorgAddonlistingLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IAddOnFolder(Interface):
    """
    Content type for add-ons folder.
    """
    #form.model("models/addonfolder.xml")


class IAddOn(Interface):
    """
    Content type for an add-on.
    """
    #form.model("models/addon.xml")


class IMapping(model.Schema):
    """
    Schema for mappings.
    """
    model.load("models/mapping.xml")


class IPyPIClassifierMapping(model.Schema):
    """
    Schema for mappings.
    """
    model.load("models/pypi_classifier_mapping.xml")


class ICategory(model.Schema):
    """
    Schema for version information.
    """
    model.load("models/category.xml")


class IVersionInfo(model.Schema):
    """
    Schema for version information.
    """
    model.load("models/versioninfo.xml")


class IVersionEggInfo(model.Schema):
    """
    Schema for version information.
    """
    model.load("models/versioninfo.xml", schema=u"egg_info")
