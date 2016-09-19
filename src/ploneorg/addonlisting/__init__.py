# -*- coding: utf-8 -*-
"""Init and utils."""


from zope.i18nmessageid import MessageFactory
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary
from zope.interface import implementer
from zope.interface import provider


_ = MessageFactory('ploneorg.addonlisting')

PYPI_URL = 'https://pypi.python.org/pypi'
