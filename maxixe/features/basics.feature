Feature: Importable features
  In order to interact programmatically with tests
  Developers should be able to import features as code

  Scenario: Found feature
    Given there is a feature
    When I attempt to import that feature like a Python file
    Then I can access it as a module
