# -*- coding: utf-8 -*-

from ploneorg.addonlisting.utils import update_addon
from ploneorg.addonlisting.utils import update_addon_list
from ploneorg.addonlisting.utils import update_addons

import argparse
import logging


logging.basicConfig()
log = logging.getLogger('ploneorg.addonlisting-cli')


def cli_update_addon_listing():
    parser = argparse.ArgumentParser(
        description="updates the listing with any new addons"
    )
    parser.add_argument(
        "context",
        help="Path to AddOnFolder relative to Zope root.\
              Ex:/Plone/<AddOnFolder name>"
    )
    parser.add_argument(
        "-v",
        "--verbose",
        default=False,
        help="print more verbose output",
        action="store_true"
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="limit the number of new addons fetched from PyPI"
    )
    parser.add_argument(
        "-s",
        "--site-id",
        dest='site_id',
        default='Plone',
        help="ID of the Plone site to fetch the content objects from"
    )
    args = parser.parse_args()

    if args.verbose:
        log.setLevel(logging.INFO)

    '''
    current = app  # noqa
    for part in site_id.split('/'):
        current = current[part]
    portal = current
    setSite(portal)
    print portal

    '''
    # obtain the portal root object somehow and
    # store in a local variable "portal"
    # log.debug(app)
    context = None
    # context = app.restrictedTraverse(args.context)

    update_addon_list(context, logger=log, limit=args.limit)


def cli_update_addons():
    parser = argparse.ArgumentParser(
        description="updates all the addons in the listing"
    )
    parser.add_argument(
        "context",
        help="Path to AddOnFolder relative to Zope root. \
              Ex:/Plone/<AddOnFolder name>"
    )
    parser.add_argument(
        "-v",
        "--verbose",
        default=False,
        help="print more verbose output",
        action="store_true"
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="limit the number of addons checked for updates from PyPI"
    )
    args = parser.parse_args()
    if args.verbose:
        log.setLevel(logging.INFO)
    context = None
    # context = portal.restrictedTraverse(args.context)
    update_addons(context, logger=log, limit=args.limit)


def cli_update_addon():
    parser = argparse.ArgumentParser(
        description="updates an individual addon"
    )
    parser.add_argument(
        "context",
        help="Path to AddOn relative to Zope root. \
              Ex:/Plone/<AddOnFolder name>/<AddOn name>"
    )
    parser.add_argument(
        "-v",
        "--verbose",
        default=False,
        help="print more verbose output",
        action="store_true"
    )
    args = parser.parse_args()
    if args.verbose:
        log.setLevel(logging.INFO)
    context = None
    # context = portal.restrictedTraverse(args.context)
    update_addon(context, logger=log)
