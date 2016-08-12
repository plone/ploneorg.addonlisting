# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from distutils.version import LooseVersion
from pkg_resources import parse_version
from plone import api
from plone.app.textfield.value import RichTextValue
from ploneorg.addonlisting import _

import logging
import requests
import simplejson as json
import urllib
import xmlrpclib


PYPI_URL = 'https://pypi.python.org/pypi'
log = logging.getLogger("ploneorg.addonlisting")


def update_addon_list(context, request=None):
    addon_folder = context

    # get Add'on List
    present_addon_list = api.content.find(context=addon_folder, portal_type="AddOn")

    client = xmlrpclib.ServerProxy(PYPI_URL)

    classifiers = context.query_classifieres if context.query_classifieres else ['Framework :: Plone']

    raw_queried_addon_list = client.browse(classifiers)

    queried_addon_list = [elem[0] for elem in raw_queried_addon_list]

    new_addons = set(queried_addon_list) - set(present_addon_list)

    if request is not None:
        request.response.write("Start Update Add'on Listing\n")
        request.response.flush()

    for elem in new_addons:
        with api.env.adopt_roles(['Manager']):
            info = u'For Add\'on-Folder: "%s" add Plone-Package "%s"' % (addon_folder.title, elem)
            log.info(info)

            if request is not None:
                request.response.write(info + "\n")
                request.response.flush()
            try:
                addon = api.content.create(
                    container=addon_folder,
                    type="AddOn",
                    id=elem,
                    title=elem
                )
            except:
                log.error(u'Could not create %s', elem)

    if request is not None:
        request.response.write("Finished Update Add'on Listing\n")
        request.response.flush()


def update_addon(context, request=None):
    addon = context
    with api.env.adopt_roles(['Manager']):

        url = PYPI_URL + '/' + addon.title + '/json'

        import ipdb; ipdb.set_trace()

        pypi_response = requests.get(url)

        if pypi_response.ok and pypi_response.status_code == 200 and \
                pypi_response.headers['Content-Type'] and \
                pypi_response.headers['Content-Type'].startswith('application/json'):
            data = pypi_response.json()

            addon.docs_link = data['info'].get('docs_link')
            addon.bugtracker_link = data['info'].get('bugtrack_link')

            if addon.description is None or addon.description == "":
                addon.description = data['info'].get('summary')

            if addon.text is None or addon.text == "":
                addon.text = RichTextValue(data['info'].get('description'), 'text/restructured', 'text/restructured')
        else:
            log.info(u'somthing went wrong on update %s', addon.title)

        if request is not None:
            request.response.redirect(context.absolute_url())


def update_addons(context, request=None):
    addon_folder = context

    # get Add'on List
    addons = api.content.find(context=addon_folder, portal_type="AddOn")

    if request is not None:
        request.response.write("Start Update all Add'ons\n")
        request.response.flush()

    for addon in addons:
        update_addon(addon, request=request)

    if request is not None:
        request.response.write("Finished Update all Add'ons\n")
        request.response.flush()
