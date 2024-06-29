Feature: Contact Form

  Scenario: Validation of required fields
    Given I am in the contact form section
    When I leave the required fields empty
    And I click the submit button
    Then I should get an error message 'Este campo es obligatorio'

  Scenario: Field formatting validation
    Given I am in the contact form section
    When in the first name field I type 'Brian'
    And in the last name field I type 'Salas'
    And in the email field I type 'Fake email'
    And in the message field I type 'This is a message'
    And I accept the terms and conditions
    And I click the submit button
    Then I should get a popup error message 'email: invalid email'