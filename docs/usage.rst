Usage
=====

There are three main groups of target users

*  Anonymous users
*  Release Team/Manager
*  Paragon/Curator team


Anonymous Users
~~~~~~~~~~~~~~~
They can see the addon listings under categories like Recommended addons, New addons and most downloaded addons.
They have the capability to filter them based on various categories.
When they click on an add-on, a modal gets displayed with more information about the add-on.
They cannot edit or add new addons.


Release Team/Manager
~~~~~~~~~~~~~~~~~~~~
They can initiate the updation of addon listing by clicking on the update_listing button.
It would call the update_listing view.
The CLI script updates the list of add-ons with new data from pypi. 
It can be used for a cron job on the setup. 
If they find a new add-on that is not tagged correctly  on PyPI,
they can add it via the add form.


Paragon/Curator team
~~~~~~~~~~~~~~~~~~~~
They can review the imported add-ons.
They can set the status of an add-on to curated,if it fits their selection criteria.
They can set the status of an add-on to blacklisted,if it is a core package or
if it is considered harmful.
They can edit the values of fields under default fieldset,
i.e data that is not retreived directly from PyPI.
