# -*- coding: utf-8 -*-

from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from ploneorg.addonlisting.interfaces import IAddOn
from ploneorg.addonlisting.interfaces import IAddOnFolder
from ploneorg.addonlisting.testing import PLONEORG_ADDONLISTING_INTEGRATION_TESTING  # noqa
from zope.component import createObject
from zope.component import queryUtility

import unittest


class AddOnIntegrationTest(unittest.TestCase):

    layer = PLONEORG_ADDONLISTING_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='AddOn')
        schema = fti.lookupSchema()
        self.assertEqual(schema, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='AddOn')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='AddOn')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(IAddOn.providedBy(obj))

    def test_adding_globaly(self):
        portal = api.portal.get()
        with self.assertRaises(ValueError,
                               message='Disallowed subobject type: AddOn'):
            self.portal.invokeFactory('AddOn', 'AddOn')

        with self.assertRaisesRegexp(InvalidParameterError,
                                     "Cannot add a 'AddOn' "
                                     'object to the container.'):
            addon = api.content.create(  # NOQA: F841
                type='AddOn',
                title='Pillow',
                container=portal
            )

    def test_adding_in_addonfolder(self):
        portal = api.portal.get()
        addon_folder = api.content.create(
            type='AddOnFolder',
            title='Plone',
            container=portal
        )

        addon = api.content.create(
            type='AddOn',
            title='Pillow',
            container=addon_folder
        )
        self.assertTrue(
            IAddOnFolder.providedBy(addon_folder)
        )
        self.assertTrue(
            IAddOn.providedBy(addon)
        )
