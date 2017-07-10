# -*- coding: utf-8 -*-

from ploneorg.addonlisting.utils import update_addon
from ploneorg.addonlisting.utils import update_addon_list
from ploneorg.addonlisting.utils import update_addons

import argparse
import logging


logging.basicConfig(level=logging.INFO)
log = logging.getLogger('ploneorg.addonlisting-cli')

'''
usage:
bin/instance -O <portal_id> update_addon_listing
                                  <Path to AddOnFolder relative to Zope root>
bin/instance -O <portal_id> update_addons
                                  <Path to AddOnFolder relative to Zope root>
bin/instance -O <portal_id> update_addon <Path to AddOn relative to Zope root>
'''


def cli_update_addon_listing(app, args):
    parser = argparse.ArgumentParser('updates the listing with new addons')
    parser.add_argument('-c')
    parser.add_argument(
        'context',
        help='Path to AddOnFolder relative to Zope root.\
              Ex:Plone/<AddOnFolder name>'
    )
    parser.add_argument(
        '-v',
        '--verbose',
        default=False,
        help='print more verbose output',
        action='store_true'
    )
    parser.add_argument(
        '--limit',
        type=int,
        default=0,
        help='limit the number of new addons fetched from PyPI'
    )
    args = parser.parse_args()
    if args.verbose:
        log.setLevel(logging.INFO)
    folder = app.unrestrictedTraverse(args.context)
    update_addon_list(folder, logger=log, limit=args.limit)


def cli_update_addons(app, args):
    parser = argparse.ArgumentParser(
        description='updates all the addons in the listing'
    )
    parser.add_argument('-c')
    parser.add_argument(
        'context',
        help='Path to AddOnFolder relative to Zope root. \
              Ex:Plone/<AddOnFolder name>'
    )
    parser.add_argument(
        '-v',
        '--verbose',
        default=False,
        help='print more verbose output',
        action='store_true'
    )
    parser.add_argument(
        '--limit',
        type=int,
        default=0,
        help='limit the number of addons checked for updates from PyPI'
    )
    args = parser.parse_args()
    if args.verbose:
        log.setLevel(logging.INFO)
    folder = app.unrestrictedTraverse(args.context)
    update_addons(folder, logger=log, limit=args.limit)


def cli_update_addon(app, args):
    parser = argparse.ArgumentParser(
        description='updates an individual addon'
    )
    parser.add_argument('-c')
    parser.add_argument(
        'context',
        help='Path to AddOn relative to Zope root. \
              Ex:/Plone/<AddOnFolder name>/<AddOn name>'
    )
    parser.add_argument(
        '-v',
        '--verbose',
        default=False,
        help='print more verbose output',
        action='store_true'
    )
    args = parser.parse_args()
    if args.verbose:
        log.setLevel(logging.INFO)
    addon = app.unrestrictedTraverse(args.context)
    update_addon(addon, logger=log)
