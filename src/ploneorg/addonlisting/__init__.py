# -*- coding: utf-8 -*-
"""Init and utils."""


from zope.i18nmessageid import MessageFactory
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
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

python_series_versions_vocabulary = SimpleVocabulary([
    SimpleTerm(value=u'python1.0', title=_(u'Python 1.0')),
    SimpleTerm(value=u'python2.0', title=_(u'Python 2.0')),
    SimpleTerm(value=u'python2.1', title=_(u'Python 2.1')),
    SimpleTerm(value=u'python2.2', title=_(u'Python 2.2')),
    SimpleTerm(value=u'python2.3', title=_(u'Python 2.3')),
    SimpleTerm(value=u'python2.4', title=_(u'Python 2.4')),
    SimpleTerm(value=u'python2.5', title=_(u'Python 2.5')),
    SimpleTerm(value=u'python2.6', title=_(u'Python 2.6')),
    SimpleTerm(value=u'python2.7', title=_(u'Python 2.7')),
    SimpleTerm(value=u'python3.0', title=_(u'Python 3.0')),
    SimpleTerm(value=u'python3.1', title=_(u'Python 3.1')),
    SimpleTerm(value=u'python3.2', title=_(u'Python 3.2')),
    SimpleTerm(value=u'python3.3', title=_(u'Python 3.3')),
    SimpleTerm(value=u'python3.4', title=_(u'Python 3.4')),
    SimpleTerm(value=u'python3.5', title=_(u'Python 3.5')),
    SimpleTerm(value=u'python3.6', title=_(u'Python 3.6')),
])


@implementer(IVocabularyFactory)
class PloneVersionsVocabulary(object):

    def __call__(self, context):
        return plone_series_versions_vocabulary

PloneVersionsVocabularyFactory = PloneVersionsVocabulary()
