@smoke
Feature: Login
  
  Background:
    Given The user is on the home page url
    When The user clicks "Signup / Login" button with link
    Then The 'Login to your account' section should be visible

  Scenario: Login User with correct email and password and logout
    When The user enters correct login name and email address
    And The user clicks on "Login" button
    Then Verify that Logged in as username is visible
    When The user clicks "Logout" button with link
    Then The 'Login to your account' section should be visible

  Scenario: Login User with incorrect email and password
    When The user enters incorrect login name and email address
    And The user clicks on "Login" button
    Then The 'Your email or password is incorrect!' section should be visible

