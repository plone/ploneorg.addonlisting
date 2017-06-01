# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from datetime import datetime
from plone import api
from plone.app.textfield.value import RichTextValue
from ploneorg.addonlisting import PYPI_URL
from ploneorg.addonlisting.contents import VersionEggInfo
from ploneorg.addonlisting.contents import VersionInfo

import logging
import requests
import transaction
import xmlrpclib


log = logging.getLogger("ploneorg.addonlisting")


def update_addon_list(context, request=None):
    addon_folder = context

    # get Add'on List
    present_addon_list = api.content.find(context=addon_folder,
                                          portal_type="AddOn")
    present_addon_list = [obj[0] for obj in context.items()]

    client = xmlrpclib.ServerProxy(PYPI_URL)

    classifiers = context.query_classifieres if context.query_classifieres else ['Framework :: Plone']  # NOQA: E501

    raw_queried_addon_list = client.browse(classifiers)

    queried_addon_list = [elem[0] for elem in raw_queried_addon_list]

    new_addons = set(queried_addon_list) - set(present_addon_list)

    if request is not None:
        request.response.write("Start Update Add'on Listing\n")

    for elem in new_addons:
        with api.env.adopt_roles(['Manager']):
            try:
                transaction.begin()
                addon = api.content.create(
                    container=addon_folder,
                    type="AddOn",
                    id=elem,
                    title=elem
                )
                transaction.get().commit()

                info = u'For Add\'on-Folder: "%s" add Plone-Package "%s"' % (addon_folder.title, elem)  # NOQA: E501
                log.info(info)
                log.info(addon)

                if request is not None:
                    request.response.write(str(info) + "\n")
            except Exception as e:
                log.error(u'Could not create %s', elem)
                log.error(e)

    if request is not None:
        request.response.write("Finished Update Add'on Listing\n")


def update_addon(context, request=None):
    addon = context
    with api.env.adopt_roles(['Manager']):
        log.info(u'Start updating: %s', addon.title)
        url = PYPI_URL + '/' + addon.title + '/json'

        pypi_response = requests.get(url)

        if pypi_response.ok and pypi_response.status_code == 200 and \
                pypi_response.headers['Content-Type'] and \
                pypi_response.headers['Content-Type'].startswith(
                'application/json'):
            data = pypi_response.json()

            if not addon.curated:
                addon.description = data['info'].get('summary')
                addon.text = RichTextValue(data['info'].get('description'),
                                           'text/restructured',
                                           'text/restructured')

            addon.current_version = data['info'].get('version')
            addon.docs_link = data['info'].get('docs_link')
            addon.bugtracker_link = data['info'].get('bugtrack_link')
            addon.author_name = data['info'].get('author')
            addon.author_email = data['info'].get('author_email')
            addon.maintainer_name = data['info'].get('maintainer')
            addon.maintainer_email = data['info'].get('maintainer_email')

            versions = []
            tsum = 0
            for version, version_data in data['releases'].iteritems():
                psum = 0
                version_info = VersionInfo()
                version_info.version_id = version
                version_info.version_name = version
                egg_infos = []
                for info in version_data:
                    egg_info = VersionEggInfo()
                    egg_info.filename = info['filename']
                    egg_info.downloads = int(info['downloads'])
                    psum += egg_info.downloads
                    egg_info.upload_time = datetime.strptime(
                        info['upload_time'], '%Y-%m-%dT%H:%M:%S').date()
                    egg_infos.append(egg_info)
                version_info.egg_files = egg_infos
                version_info.downloads = psum
                tsum += psum
                versions.append(version_info)
            addon.downloads = tsum
            addon.versions = versions

            api.portal.show_message("Add'on %s has been updated" %
                                    (addon.title),
                                    request=request, type='info')
            log.info(u'Finished to update: %s', addon.title)
        else:
            log.info(u'something went wrong on update %s', addon.title)

        if request is not None:
            request.response.redirect(context.absolute_url())


def update_addons(context, request=None):
    addon_folder = context

    # get Add'on List
    addons = api.content.find(context=addon_folder, portal_type="AddOn")

    if request is not None:
        request.response.write("Start Update all Add-ons\n")

    for addon in addons:
        update_addon(addon, request=request)

    if request is not None:
        request.response.write("Finished Update all Add-ons\n")
