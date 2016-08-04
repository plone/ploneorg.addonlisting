# -*- coding: utf-8 -*-
"""Init and utils."""


from zope.i18nmessageid import MessageFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

_ = MessageFactory('ploneorg.addonlisting')


plone_series_versions_vocabulary = SimpleVocabulary([
    SimpleTerm(value=u'plone1.0', title=_(u'Plone 1.0')),
    SimpleTerm(value=u'plone2.0', title=_(u'Plone 2.0')),
    SimpleTerm(value=u'plone2.1', title=_(u'Plone 2.1')),
    SimpleTerm(value=u'plone2.5', title=_(u'Plone 2.5')),
    SimpleTerm(value=u'plone3.0', title=_(u'Plone 3.0')),
    SimpleTerm(value=u'plone3.1', title=_(u'Plone 3.1')),
    SimpleTerm(value=u'plone3.2', title=_(u'Plone 3.2')),
    SimpleTerm(value=u'plone3.3', title=_(u'Plone 3.3')),
    SimpleTerm(value=u'plone4.0', title=_(u'Plone 4.0')),
    SimpleTerm(value=u'plone4.1', title=_(u'Plone 4.1')),
    SimpleTerm(value=u'plone4.2', title=_(u'Plone 4.2')),
    SimpleTerm(value=u'plone4.3', title=_(u'Plone 4.3')),
    SimpleTerm(value=u'plone5.0', title=_(u'Plone 5.0')),
    SimpleTerm(value=u'plone5.1', title=_(u'Plone 5.1'))
])
