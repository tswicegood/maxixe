Feature: Importable features
  In order to interact programmatically with tests
  Developers should be able to import features as code

  Scenario: Found feature
    Given there is a feature
    When I attempt to import that feature like a Python file
    Then I can access it as a module

  Scenario: Steps that aren't implemented
    Given there is a feature
    When I import the feature
    Then I can see what steps are not runnable

  Scenario: First step is not defined
    Given I have a scenario with an undefined first step
    When I check to see to see if the scenario is runnable
    Then I am told it is not
    And I can access it as a module
