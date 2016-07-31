# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from ploneorg.addonlisting.testing import PLONEORG_ADDONLISTING_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that ploneorg.addonlisting is properly installed."""

    layer = PLONEORG_ADDONLISTING_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if ploneorg.addonlisting is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'ploneorg.addonlisting'))

    def test_browserlayer(self):
        """Test that IPloneorgAddonlistingLayer is registered."""
        from ploneorg.addonlisting.interfaces import (
            IPloneorgAddonlistingLayer)
        from plone.browserlayer import utils
        self.assertIn(IPloneorgAddonlistingLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONEORG_ADDONLISTING_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['ploneorg.addonlisting'])

    def test_product_uninstalled(self):
        """Test if ploneorg.addonlisting is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'ploneorg.addonlisting'))

    def test_browserlayer_removed(self):
        """Test that IPloneorgAddonlistingLayer is removed."""
        from ploneorg.addonlisting.interfaces import IPloneorgAddonlistingLayer
        from plone.browserlayer import utils
        self.assertNotIn(IPloneorgAddonlistingLayer, utils.registered_layers())
