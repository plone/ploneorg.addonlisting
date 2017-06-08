from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from ploneorg.addonlisting.interfaces import IAddOn
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

    def test_adding(self):
        self.portal.invokeFactory('AddOn', 'AddOn')
        self.assertTrue(
            IAddOn.providedBy(self.portal['AddOn'])
        )
