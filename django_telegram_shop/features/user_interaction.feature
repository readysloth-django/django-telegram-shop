Feature: User interaction with Bot

  User can call various menus that send back messages and
  keyboards.

  Scenario: Main menu
    Given telegram bot
    When start_bot called
    Then process should spawn
    When 'user' started interaction
    Then 'user' should receive keyboard
