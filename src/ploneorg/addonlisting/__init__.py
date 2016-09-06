# -*- coding: utf-8 -*-
"""Init and utils."""


from zope.i18nmessageid import MessageFactory
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary
from zope.interface import directlyProvides


_ = MessageFactory('ploneorg.addonlisting')

PYPI_URL = 'https://pypi.python.org/pypi'

state_vocabulary = SimpleVocabulary([
    SimpleTerm(value=u'alpha', title=_(u'Alpha Status (Prototype State, never use in Production)')),
    SimpleTerm(value=u'beta', title=_(u'Beta Status (Development State / Release preperations)')),
    SimpleTerm(value=u'stable', title=_(u'Production/Stable')),
    SimpleTerm(value=u'unmaintained', title=_(u'Unmaintained/Inactive ()')),
])


@implementer(IVocabularyFactory)
class PloneVersionsVocabulary(object):

    def __call__(self, context):
        return plone_series_versions_vocabulary

PloneVersionsVocabularyFactory = PloneVersionsVocabulary()


@implementer(IVocabularyFactory)
class FrameworkVersionsDynamicVocabulary(object):

    def __call__(self, context):
        terms = []
        if context:
            versions = context.framework_version_mapping
            for version in versions:
                terms.append(SimpleVocabulary.createTerm(version['key'], version['value']))
        return SimpleVocabulary(terms)

FrameworkVersionsDynamicVocabularyFactory = FrameworkVersionsDynamicVocabulary()


@implementer(IVocabularyFactory)
class PythonVersionsDynamicVocabulary(object):

    def __call__(self, context):
        terms = []
        if context:
            versions = context.python_version_mapping
            for version in versions:
                terms.append(SimpleVocabulary.createTerm(version['key'], version['value']))
        return SimpleVocabulary(terms)

PythonVersionsDynamicVocabularyFactory = PythonVersionsDynamicVocabulary()


@implementer(IVocabularyFactory)
class StateVocabulary(object):

    def __call__(self, context):
        return state_vocabulary

StateVocabularyFactory = StateVocabulary()
