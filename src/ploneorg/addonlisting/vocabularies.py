# -*- coding: utf-8 -*-
"""static and dynamic vocabularies."""

# flake8: NOQA: E501

from ploneorg.addonlisting import _
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


@provider(IVocabularyFactory)
def framework_versions_dynamic_vocabulary(context):
    terms = []
    if context:
        versions = context.framework_version_mapping
        for version in versions:
            terms.append(SimpleVocabulary.createTerm(version['key'], version['value']))
    return SimpleVocabulary(terms)


@provider(IVocabularyFactory)
def python_versions_dynamic_vocabulary(context):
    terms = []
    if context:
        versions = context.python_version_mapping
        for version in versions:
            terms.append(SimpleVocabulary.createTerm(version['key'], version['value']))
    return SimpleVocabulary(terms)


@provider(IVocabularyFactory)
def addon_type_vocabulary(context):
    terms = []
    if context:
        types = context.add_categories
        for cat in types:
            terms.append(SimpleVocabulary.createTerm(cat, cat))
    return SimpleVocabulary(terms)


@provider(IVocabularyFactory)
def addon_pypi_state_vocabulary(context):
    return SimpleVocabulary([
        SimpleTerm(value=u'status-1', title=u'Development Status :: 1 - Planning'),
        SimpleTerm(value=u'status-2', title=u'Development Status :: 2 - Pre-Alpha'),
        SimpleTerm(value=u'status-3', title=u'Development Status :: 3 - Alpha'),
        SimpleTerm(value=u'status-4', title=u'Development Status :: 4 - Beta'),
        SimpleTerm(value=u'status-5', title=u'Development Status :: 5 - Production/Stable'),
        SimpleTerm(value=u'status-6', title=u'Development Status :: 6 - Mature'),
        SimpleTerm(value=u'status-7', title=u'Development Status :: 7 - Inactive'),
    ])


@provider(IVocabularyFactory)
def addon_state_vocabulary(context):
    return SimpleVocabulary([
        SimpleTerm(value=u'alpha', title=_(u'Alpha status (prototype state: never use in production)')),
        SimpleTerm(value=u'beta', title=_(u'Beta status (development state: release being prepared)')),
        SimpleTerm(value=u'stable', title=_(u'Production/Stable')),
        SimpleTerm(value=u'unmaintained', title=_(u'Unmaintained/Inactive ()')),
    ])
