@regression_tests

Feature: Validate menu options redirection

  Scenario: Click on each menu option and verify redirection
    Given I navigate to the kayak main page
    Then I should be in the "home" page
    When I click on each menu option
    Then I should be redirected to the corresponding page
