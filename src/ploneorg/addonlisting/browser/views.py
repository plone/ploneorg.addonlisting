# -*- coding: utf-8 -*-

from plone import api
from plone.protect.interfaces import IDisableCSRFProtection
from ploneorg.addonlisting.contents import FilterForm
from ploneorg.addonlisting.utils import update_addon
from ploneorg.addonlisting.utils import update_addon_list
from ploneorg.addonlisting.utils import update_addons
from Products.CMFPlone.resources import add_resource_on_request
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.interface import alsoProvides

import logging


logging.basicConfig(level=logging.INFO)
log = logging.getLogger('ploneorg.addonlisting')
limit = 10


def html_header(title=''):
    return """
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>{title}</title>
  </head>
  <body>
    <pre>
""".format(title=title)


def html_footer(url=''):
    return """
    </pre>
    <script type="text/javascript" >
      window.location.href = "{url}";
    </script>
  </body>
</html>
""".format(url=url)


class FolderUpdateView(BrowserView):
    def __call__(self):
        url = self.context.absolute_url()
        alsoProvides(self.request, IDisableCSRFProtection)
        self.request.response.setHeader(
            'Content-type',
            'text/html; charset=utf-8',
        )
        log.addHandler(logging.StreamHandler(self.request.response))
        log.info(html_header('Update Folder'))
        update_addon_list(self.context, logger=log)
        log.info(html_footer(url))


class FolderUpdateAllView(BrowserView):
    def __call__(self):
        url = self.context.absolute_url()
        alsoProvides(self.request, IDisableCSRFProtection)
        self.request.response.setHeader(
            'Content-type',
            'text/html; charset=utf-8',
        )
        log.addHandler(logging.StreamHandler(self.request.response))
        log.info(html_header('Update Folder'))
        update_addon_list(self.context, logger=log)
        update_addons(self.context, logger=log)
        log.info(html_footer(url))


class AddOnUpdateView(BrowserView):
    def __call__(self):
        url = self.context.absolute_url()
        alsoProvides(self.request, IDisableCSRFProtection)
        self.request.response.setHeader(
            'Content-type',
            'text/html; charset=utf-8',
        )
        log.addHandler(logging.StreamHandler(self.request.response))
        log.info(html_header('Update Folder'))
        update_addon(self.context, logger=log)
        api.portal.show_message(
            "Add'on {title} has been updated".format(title=self.context.title),
            request=self.request,
            type='info',
        )
        log.info(html_footer(url))


class AddOnView(BrowserView):
    template = ViewPageTemplateFile('templates/addon_view.pt')

    def __call__(self):
        return self.template()


class AddOnFolderView(BrowserView):
    def __call__(self):
        add_resource_on_request(self.request, 'ploneorg-addonlisting')
        return super(AddOnFolderView, self).__call__()

    def curated_addons(self):
        return api.content.find(
            context=self.context,
            depth=1,
            portal_type='AddOn',
            curated=True,
            sort_on='sortable_title',
            sort_order='ascending',
            sort_limit=limit
        )[:limit]

    def downloaded_addons(self):
        return api.content.find(
            context=self.context,
            depth=1,
            portal_type='AddOn',
            blacklisted=False,
            sort_on='download_sum_total',
            sort_order='reverse',
            sort_limit=limit
        )[:limit]

    def new_addons(self):
        return api.content.find(
            context=self.context,
            depth=1,
            portal_type='AddOn',
            blacklisted=False,
            sort_on='upload_time',
            sort_order='reverse',
            sort_limit=limit
        )[:limit]


class FilteredAddOnFolderView(AddOnFolderView):

    def __call__(self):
        add_resource_on_request(self.request, 'ploneorg-addonlisting')
        return super(FilteredAddOnFolderView, self).__call__()

    def filter_form(self):
        form = FilterForm(self.context, self.request)
        form.update()
        return form

    def __call__(self):
        if self.request.method == 'POST':
            self.filter = {
                'curated': bool(self.request.form.get('form.widgets.curated')),
                'blacklisted': bool(self.request.form.get(
                    'form.widgets.blacklisted')),
                'addon_type': self.request.form.get(
                    'form.widgets.addon_type'),
                'addon_status': self.request.form.get(
                    'form.widgets.addon_status'),
                'supported_python_versions': self.request.form.get(
                    'form.widgets.supported_python_versions'),
                'supported_framework_versions': self.request.form.get(
                    'form.widgets.supported_framework_versions')
            }
        else:
            self.filter = dict()
        return super(FilteredAddOnFolderView, self).__call__()

    def all_addons(self):
        if self.filter:
            if self.filter.get('curated'):
                return api.content.find(
                    context=self.context,
                    depth=1,
                    portal_type='AddOn',
                    curated=self.filter.get('curated'),
                    blacklisted=self.filter.get('blacklisted'),
                    addon_status=self.filter.get('curated_status'),
                    addon_type=self.filter.get('addon_type'),
                    supported_python_versions={
                        'query': self.filter.get('supported_python_versions'),
                        'operator': 'and'
                    },
                    supported_framework_versions={
                        'query': self.filter.get(
                            'supported_framework_versions'
                        ),
                        'operator': 'and'
                    },
                    sort_on='sortable_title',
                    sort_order='ascending'
                )
            else:
                return api.content.find(
                    context=self.context,
                    depth=1,
                    portal_type='AddOn',
                    curated=self.filter.get('curated'),
                    blacklisted=self.filter.get('blacklisted'),
                    addon_status=self.filter.get('pypi_status'),
                    addon_type=self.filter.get('addon_type'),
                    supported_python_versions={
                        'query': self.filter.get('supported_python_versions'),
                        'operator': 'and'
                    },
                    supported_framework_versions={
                        'query': self.filter.get(
                            'supported_framework_versions'
                        ),
                        'operator': 'and'
                    },
                    sort_on='sortable_title',
                    sort_order='ascending'
                )
        return api.content.find(
            context=self.context,
            depth=1,
            portal_type='AddOn',
            sort_on='sortable_title',
            sort_order='ascending'
        )

    def downloaded_addons(self):
        if self.filter:
            if self.filter.get('curated'):
                return api.content.find(
                    context=self.context,
                    depth=1,
                    portal_type='AddOn',
                    curated=self.filter.get('curated'),
                    blacklisted=self.filter.get('blacklisted'),
                    addon_status=self.filter.get('curated_status'),
                    addon_type=self.filter.get('addon_type'),
                    supported_python_versions={
                        'query': self.filter.get('supported_python_versions'),
                        'operator': 'and'
                    },
                    supported_framework_versions={
                        'query': self.filter.get(
                            'supported_framework_versions'
                        ),
                        'operator': 'and'
                    },
                    sort_on='download_sum_total',
                    sort_order='reverse'
                )
            else:
                return api.content.find(
                    context=self.context,
                    depth=1,
                    portal_type='AddOn',
                    curated=self.filter.get('curated'),
                    blacklisted=self.filter.get('blacklisted'),
                    addon_status=self.filter.get('pypi_status'),
                    addon_type=self.filter.get('addon_type'),
                    supported_python_versions={
                        'query': self.filter.get('supported_python_versions'),
                        'operator': 'and'
                    },
                    supported_framework_versions={
                        'query': self.filter.get(
                            'supported_framework_versions'
                        ),
                        'operator': 'and'
                    },
                    sort_on='download_sum_total',
                    sort_order='reverse'
                )
        return api.content.find(
            context=self.context,
            depth=1,
            portal_type='AddOn',
            sort_on='download_sum_total',
            sort_order='reverse'
        )

    def new_addons(self):
        if self.filter:
            if self.filter.get('curated'):
                return api.content.find(
                    context=self.context,
                    depth=1,
                    portal_type='AddOn',
                    curated=self.filter.get('curated'),
                    blacklisted=self.filter.get('blacklisted'),
                    curated_status=self.filter.get('curated_status'),
                    supported_python_versions={
                        'query': self.filter.get('supported_python_versions'),
                        'operator': 'and'
                    },
                    supported_framework_versions={
                        'query': self.filter.get(
                            'supported_framework_versions'
                        ),
                        'operator': 'and'
                    },
                    addon_type=self.filter.get('addon_type'),
                    sort_on='upload_time',
                    sort_order='reverse'
                )
            else:
                return api.content.find(
                    context=self.context,
                    depth=1,
                    portal_type='AddOn',
                    curated=self.filter.get('curated'),
                    blacklisted=self.filter.get('blacklisted'),
                    curated_status=self.filter.get('pypi_status'),
                    supported_python_versions={
                        'query': self.filter.get('supported_python_versions'),
                        'operator': 'and'
                    },
                    supported_framework_versions={
                        'query': self.filter.get(
                            'supported_framework_versions'
                        ),
                        'operator': 'and'
                    },
                    addon_type=self.filter.get('addon_type'),
                    sort_on='upload_time',
                    sort_order='reverse'
                )
        return api.content.find(
            context=self.context,
            depth=1,
            portal_type='AddOn',
            sort_on='upload_time',
            sort_order='reverse'
        )
