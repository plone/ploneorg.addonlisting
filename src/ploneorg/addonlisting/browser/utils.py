# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from plone import api
from ploneorg.addonlisting import _

import simplejson as json
import xmlrpclib
import urllib
import requests


pypi_url = 'https://pypi.python.org/pypi'


def update_addon_list(context):
    # get Add'on List
    present_addon_list = api.content.find(context=context, portal_type="AddOn")

    client = xmlrpclib.ServerProxy(pypi_url)

    raw_queried_addon_list = client.browse([
        'Framework :: Plone',
        #'Environment :: Plugins',
    ])

    queried_addon_list = [elem[0] for elem in raw_queried_addon_list]

    new_addons = set(queried_addon_list) - set(present_addon_list)

    for elem in new_addons:
        with api.env.adopt_roles(['Manager']):

            url = pypi_url + '/' + elem + '/json'

            import ipdb; ipdb.set_trace()

            pypi_response = requests.get(url)

            if pypi_response.ok and pypi_response.status_code == 200 and pypi_response.header['Content-Type'] == 'application/json':
                data = pypi_response.json()


                addon = api.content.create(
                    container=context,
                    type="AddOn",
                    id=elem,
                    title=elem
                )
                addon.name
