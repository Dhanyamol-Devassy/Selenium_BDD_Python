@smoke
Feature: ContactUs
  
  Background:
    Given The user is on the home page url
  Scenario:
    When The user clicks "Contact us" button with link
    Then The "GET IN TOUCH" header should be visible

    When The user fills in contact us information
    And Click OK button in the prompt
    Then The 'Success! Your details have been submitted successfully.' section should be visible

    When The user clicks "Home" button with link
    Then Verify the user is on the home page

