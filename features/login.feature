Feature: Verify that Login Functionality is working fine

  Scenario Outline: Test Login page with Invalid data
    Given I click on the Login link in the Home page
    When I enter invalid <username> username
    Then I enter invalid <password> password
    Then I submit login details
    Then I close the login popup
    Examples:
    |username|password|
    |hi      |pwd     |

  Scenario: Test that Registration page is opened correctly
    Given I click on the JoinNow link in the Home page
    Then I should see the registration page is opened in the same tab
