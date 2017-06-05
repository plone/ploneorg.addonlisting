Implementation of ploneorg.addonlisting 
===============================================================

Plone Dexterity Content type is used to store the add-on data locally.

The custom content type addOn consists of the following fields:

* title – Name of the add-on and it is a mandatory field.
* description - A one-line description for the add-on (up to 120 characters); if not specified,
  the PyPi short description will be used.
* text - A longer, friendly description of the add-on; if not specified, 
  the PyPi description will be used. 
* curated – Boolean value to determine whether the addon is curated or not. This field would be updated 
  by a member of the paragon/curator team. Setting the value to 'True' would make it a recommended add-on.
* blacklisted -  Boolean value to determine whether the addon is blacklisted or not. This includes core 
  addons and addons that might be harmful. Setting the value to 'True' would prevent it from being displayed in the listing. 
* curated_status – To determine whether the add-on is in a workable state. It can take one of the values from Planning,
  Pre-Alpha, Alpha, Beta, Production/Stable, Mature, Inactive.
* addon_type – To choose categories for the add-on that helps in filtering them.

  and the following fields are automatically updated from PyPI,
  
* current_version – The latest release version of this add-on.
* pypi_status – To determine the PyPI status of the addon. It can take one of the values from Planning,
  Pre-Alpha, Alpha, Beta, Production/Stable, Mature, Inactive.
* supported_framework_versions – A list of supported framework versions.
* supported_python_versions - A list of supported python versions.
* keywords – A list of keywords assosciated with the add-on.
* author_name – Name of the add-on author
* author_email – Email of the add-on author
* maintainer_name – Name of the add-on maintainer
* maintainer_email – Email of the add-on maintainer
* docs_link – Link to this add-on's documentation
* bugtracker_link – Link to this add-on's issue tracker
* versions -  A list of supported plone versions
* docs_link – Link to this add-on's documentation
* package_url – Link to this addon's pypi page
* release_url – Link to this addon's release page
* home_page – Link to this addon's home page
* platform – List of compatible platforms
* license - License assosciated with the addon
* downloads - Number of downloads of this addon. It is used to sort the addons based on their download numbers.
* upload_time - upload time of the first version of this addon to find whether it is a new addon. It is used to
  find the newest addons to be displayed. 
* cheesecake_code_kwalitee_id – It refers to the code kwalitee index of the package computed by the cheeescake script.
* cheesecake_installability_id – It refers to the installability index of the package computed by the cheesecake script.
* cheesecake_documentation_id – It refers to the documentation index of the package computed by the cheesecake script.

Cheesecake project  ranks Python packages based on various empirical “kwalitee” factors, such as:

* whether the package can be downloaded from PyPI given its name
* whether the package can be unpacked
* whether the package can be installed into an alternate directory
* existence of certain files such as README, INSTALL, LICENSE, setup.py etc.
* percentage of modules/functions/classes/methods with docstrings
* pylint score
* and many others

The final score depends on how well the package scores for all indexes listed above. The relative score  (percent of 
points obtained compared to maximum possible points) can help the curator in determining  the goodness of the add-on.
More details about the cheesecake package at (https://pypi.python.org/pypi/Cheesecake)
