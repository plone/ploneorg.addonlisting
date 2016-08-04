# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from ploneorg.addonlisting.browser.utils import update_addon_list


class FolderUpdateView(BrowserView):

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        update_addon_list(self.context)
