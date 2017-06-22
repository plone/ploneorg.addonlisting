# -*- coding: utf-8 -*-
from plone import api
from plone.protect.interfaces import IDisableCSRFProtection
from ploneorg.addonlisting.utils import update_addon
from ploneorg.addonlisting.utils import update_addon_list
from ploneorg.addonlisting.utils import update_addons
from Products.CMFPlone.resources import add_resource_on_request
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.interface import alsoProvides


class FolderUpdateView(BrowserView):
    def __call__(self):
        alsoProvides(self.request, IDisableCSRFProtection)
        update_addon_list(self.context, self.request)
        # return self.request.response.redirect(self.context.absolut_url)


class FolderUpdateAllView(BrowserView):
    def __call__(self):
        alsoProvides(self.request, IDisableCSRFProtection)
        update_addon_list(self.context, self.request)
        update_addons(self.context, self.request)


class AddOnUpdateView(BrowserView):
    def __call__(self):
        alsoProvides(self.request, IDisableCSRFProtection)
        update_addon(self.context, self.request)


class AddOnView(BrowserView):
    template = ViewPageTemplateFile('templates/addon_view.pt')

    def __call__(self):
        return self.template()


class AddOnFolderView(BrowserView):
    def __call__(self):
        add_resource_on_request(self.request, 'myresources')
        return super(AddOnFolderView, self).__call__()

    def curated_addons(self):
        return api.content.find(
            context=self.context,
            depth=1,
            portal_type='AddOn',
            curated=True,
            sort_on='sortable_title',
            sort_order='ascending'
        )
        
    def downloaded_addons(self):
        return api.content.find(
            context=self.context,
            depth=1,
            portal_type='AddOn',
            blacklisted=False,
            sort_on='download_sum_total',
            sort_order='reverse'
        )


    def new_addons(self):
        return api.content.find(
            context=self.context,
            depth=1,
            portal_type='AddOn',
            blacklisted=False,
            sort_on='upload_time',
            sort_order='reverse'
        )
