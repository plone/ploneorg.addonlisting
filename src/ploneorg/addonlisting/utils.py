# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from datetime import datetime
from plone import api
from plone.app.textfield.value import RichTextValue
from ploneorg.addonlisting import PYPI_URL
from ploneorg.addonlisting.contents import VersionEggInfo
from ploneorg.addonlisting.contents import VersionInfo
from zExceptions import BadRequest

import requests
import xmlrpclib


def update_addon_list(context, logger, limit=0):
    addon_folder = context

    # get Add'on List
    present_addon_list = api.content.find(context=addon_folder,
                                          portal_type='AddOn')
    present_addon_list = [obj[0] for obj in context.items()]

    client = xmlrpclib.ServerProxy(PYPI_URL)
    classifiers = context.query_classifieres if context.query_classifieres else ['Framework :: Plone']  # NOQA: E501
    raw_queried_addon_list = client.browse(classifiers)
    queried_addon_list = [elem[0] for elem in raw_queried_addon_list]
    new_addons = set(queried_addon_list) - set(present_addon_list)

    if limit:
        new_addons = list(new_addons)[:limit]

    logger.info('Start Update Add\'on Listing')
    for elem in new_addons:
        with api.env.adopt_roles(['Manager']):
            try:
                addon = api.content.create(
                    container=addon_folder,
                    type='AddOn',
                    id=elem,
                    title=elem,
                )

                info = 'For Add\'on-Folder: "{title}" add PyPI-Package "{package}"'.format(  # NOQA: E501
                    title=str(addon_folder.title),
                    package=str(elem),
                )
                logger.info(info)
                logger.info(addon)

            except BadRequest as e:
                logger.error('Could not create %s', str(elem))
                logger.error(e)

    logger.info("Finished Update Add'on Listing")


def update_addon(context, logger):
    addon = context

    with api.env.adopt_roles(['Manager']):
        logger.info('Start trying updating: %s', str(addon.title))

        url = PYPI_URL + '/' + addon.title + '/json'
        headers = {
            'Accept': 'application/json',
            'user-agent': 'Plone-AddonListing-Bot',
        }
        pypi_response = requests.get(url, headers=headers)

        if pypi_response.ok and pypi_response.status_code == 200 and \
                pypi_response.headers['Content-Type'] and \
                pypi_response.headers['Content-Type'].startswith(
                    'application/json',
                ):
            data = pypi_response.json()

            if not addon.curated:
                addon.description = data['info'].get('summary')
                addon.text = RichTextValue(
                    raw=data['info'].get('description'),
                    mimeType='text/restructured',
                    outputMimeType='text/x-html-safe',
                )

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
                    logger.info(str(info['downloads']))
                    psum += egg_info.downloads
                    logger.info(str(info['upload_time']))
                    egg_info.upload_time = datetime.strptime(
                        info['upload_time'], '%Y-%m-%dT%H:%M:%S').date()
                    egg_infos.append(egg_info)
                version_info.egg_files = egg_infos
                version_info.downloads = psum
                tsum += psum
                versions.append(version_info)
            addon.downloads = tsum
            addon.versions = versions

            logger.info('Finished to update: %s', str(addon.title))
        else:
            logger.info('something went wrong on update %s', str(addon.title))


def update_addons(context, logger, limit=0):
    addon_folder = context

    if limit:
        addons = api.content.find(
            context=addon_folder,
            portal_type='AddOn',
            sort_limit=limit,
        )[:limit]
    else:
        addons = api.content.find(
            context=addon_folder,
            portal_type='AddOn',
        )

    logger.info('Start Update all Add-ons\n')

    for addon in addons:
        update_addon(addon.getObject(), logger=logger)

    logger.info('Finished Update all Add-ons\n')
