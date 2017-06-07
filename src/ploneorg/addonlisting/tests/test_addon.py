from pkg_resources import resource_stream
from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles
from plone.dexterity.interfaces import IDexterityFTI
from ploneorg.addonlisting.testing import PLONEORG_ADDONLISTING_INTEGRATION_TESTING
from zope.component import createObject
from zope.component import queryUtility
import unittest


class AddOnIntegrationTest(unittest.TestCase):

    layer = PLONEORG_ADDONLISTING_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='AddOn')
        self.assertTrue(fti)

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='AddOn')
        schema = fti.lookupSchema()
        self.assertTrue(schema)
        

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='AddOn')
        factory = fti.factory
        AddOn = createObject(factory)
        self.assertTrue(AddOn)

    def test_adding(self):
        self.portal.invokeFactory('AddOn', 'AddOn')
        self.assertTrue(self.portal.AddOn)
        