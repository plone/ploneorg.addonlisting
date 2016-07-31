# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s ploneorg.addonlisting -t test_addonfolder.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src ploneorg.addonlisting.testing.PLONEORG_ADDONLISTING_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_addonfolder.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a AddOnFolder
  Given a logged-in site administrator
    and an add addonfolder form
   When I type 'My AddOnFolder' into the title field
    and I submit the form
   Then a addonfolder with the title 'My AddOnFolder' has been created

Scenario: As a site administrator I can view a AddOnFolder
  Given a logged-in site administrator
    and a addonfolder 'My AddOnFolder'
   When I go to the addonfolder view
   Then I can see the addonfolder title 'My AddOnFolder'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add addonfolder form
  Go To  ${PLONE_URL}/++add++AddOnFolder

a addonfolder 'My AddOnFolder'
  Create content  type=AddOnFolder  id=my-addonfolder  title=My AddOnFolder


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the addonfolder view
  Go To  ${PLONE_URL}/my-addonfolder
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a addonfolder with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the addonfolder title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
