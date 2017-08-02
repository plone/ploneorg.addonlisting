# -*- coding: utf-8 -*-
"""Installer for the ploneorg.addonlisting package."""

from setuptools import find_packages
from setuptools import setup


long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name='ploneorg.addonlisting',
    version='1.0a1',
    description='Add-on listings for Plone.org',
    long_description=long_description,
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Plone',
        'Framework :: Plone :: 5.1',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
    ],
    keywords='Python Plone',
    author='Alexander Loechel - Plone Foundation',
    author_email='Alexander.Loechel@lmu.de',
    maintainer='Plone Foundation',
    maintainer_email='plone-developers@lists.sourceforge.net',
    url='https://pypi.python.org/pypi/ploneorg.addonlisting',
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['ploneorg'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'plone.api',
        'Products.GenericSetup>=1.8.2',
        'plone.app.dexterity',
        'plone.supermodel',
        'z3c.jbot',
        'collective.z3cform.datagridfield',
        'requests',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            # Plone KGS does not use this version, because it would break
            # Remove if your package shall be part of coredev.
            # plone_coredev tests as of 2016-04-01.
            'plone.testing>=5.0.0',
            'plone.app.contenttypes',
            'plone.app.robotframework[debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [zopectl.command]
    update_addon_listing = ploneorg.addonlisting.cli:cli_update_addon_listing
    update_addons = ploneorg.addonlisting.cli:cli_update_addons
    update_addon = ploneorg.addonlisting.cli:cli_update_addon
    """,
)
