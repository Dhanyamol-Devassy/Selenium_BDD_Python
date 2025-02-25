@smoke
Feature: Testcases page

  Scenario: Verify testcases page

    Given The user is on the home page url
    When The user clicks "Test Cases" button with link
    Then Verify the user is on the "test_cases" page
    And The "Below is the list of test Cases for you to practice the Automation" section should be visible