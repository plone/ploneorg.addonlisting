Aim of ploneorg.addonlisting 
===============================================================

ploneorg.addonlisting creates an add-on listing for Plone.org that would be more helpful to Plone users, 
in finding relevant add-ons. It would allow highlighting of curated add-ons (editor's choice), simpler 
descriptions of add-ons with relevant tags(categories), version compatibility and filtering based on these fields. 

ploneorg.addonlisting uses cron job to retrieve the add-on listing data from PyPI and store the data locally 
in Plone. The data is used to update the listings at plone.org. This solves the problem of manually
maintaining the add-on list.