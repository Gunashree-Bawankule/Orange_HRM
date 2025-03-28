Feature: OrangeHRM Login functionality

  Scenario Outline: Successfully Login with valid credentials into OrangeHRM
    Given user is on the login page
    When user enter valid <username> and <password>
    And user click on the login button
    Then user should be redirected to the dashboard

    Examples:
      | username | password |
      | Admin    | admin123 |

  Scenario Outline: User fails to log into OrangeHRM with invalid credentials
    Given user is on the login page
    When the user enters invalid <invalid_username> and <invalid_password>
    And user click on the login button
    Then the user should see an error message

    Examples:
      | invalid_username | invalid_password |
      | Sales            | sales123         |

  Scenario Outline: User forgets password and requests a password reset
    Given user is on the login page
    When user click on the forget password link
    And user enters the registered <username>
    And user click on the "Reset Password" button
    Then user should see a confirmation message

    Examples:
      | username |
      | Admin    |
      | Sales    |
