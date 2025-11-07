# Created by lgodi at 10/22/2025
Feature: Tests for Community page
  #Testing Community page

  Scenario: User can open the Community page
    Given Open reely signin page
    When Input valid credentials
    And Click Continue button
    And Click Settings option
    And Click Community option
    Then Verify Community page opens
    And Verify Contact support button is available

#  Mobile scenario
  Scenario: User can open the Community page (Mobile)
    Given Open reely signin page
    When Input valid credentials
    And Click Continue button
    And Click Menu option
    And Click Community option
    Then Verify Community page opens
    And Verify Contact support button is available


