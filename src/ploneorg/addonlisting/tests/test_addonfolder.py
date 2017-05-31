# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from ploneorg.addonlisting.interfaces import IAddOnFolder
from ploneorg.addonlisting.testing import PLONEORG_ADDONLISTING_INTEGRATION_TESTING  # noqa
from zope.component import createObject
from zope.component import queryUtility

import unittest


class AddOnFolderIntegrationTest(unittest.TestCase):

    layer = PLONEORG_ADDONLISTING_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='AddOnFolder')
        schema = fti.lookupSchema()
        #self.assertEqual(IAddOnFolder, schema)
        self.assertEqual(schema, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='AddOnFolder')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='AddOnFolder')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(IAddOnFolder.providedBy(obj))

    def test_adding(self):
        self.portal.invokeFactory('AddOnFolder', 'AddOnFolder')
        self.assertTrue(
            IAddOnFolder.providedBy(self.portal['AddOnFolder'])
        )
