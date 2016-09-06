# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from ploneorg.addonlisting.browser.utils import update_addon
from ploneorg.addonlisting.browser.utils import update_addon_list
from plone.protect.interfaces import IDisableCSRFProtection
from zope.interface import alsoProvides


class FolderUpdateView(BrowserView):

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        alsoProvides(self.request, IDisableCSRFProtection)
        update_addon_list(self.context, self.request)


class FolderUpdateAllView(BrowserView):

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        alsoProvides(self.request, IDisableCSRFProtection)
        update_addon_list(self.context, self.request)


class AddOnUpdateView(BrowserView):

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        alsoProvides(self.request, IDisableCSRFProtection)
        update_addon(self.context, self.request)


class AddOnView(BrowserView):

    template = ViewPageTemplateFile('templates/addon_view.pt')

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        return self.template()


class AddOnBaseView(BrowserView):

    template = ViewPageTemplateFile('templates/addon_base_view.pt')

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        return self.template()
