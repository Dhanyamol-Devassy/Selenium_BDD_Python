
@smoke
Feature: Register

  Background:
    Given The user is on the home page url
    When The user clicks "Signup / Login" button with link
    Then The 'New User Signup!' section should be visible
  
  Scenario: Register User Successfully
    #the email and user name are generated randomly
    When The user enters name and email address
    And The user clicks on "Signup" button
    Then The "ENTER ACCOUNT INFORMATION" header should be visible

    When The user fills in account information
    Then The "ACCOUNT CREATED!" header should be visible

    When The user clicks "Continue" button with link
    Then Verify that Logged in as username is visible 

    When The user clicks "Delete Account" button with link
    Then The "ACCOUNT DELETED!" header should be visible

  Scenario: Register with existing email address
    #here the user email already exist and is read from the test data json
    When The user enters name and email address from test data
    And The user clicks on "Signup" button
    Then The 'Email Address already exist!' section should be visible


  



