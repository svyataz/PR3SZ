Feature: inspection

    Scenario: Diagnosis:accident cerebrovascular with miss input
        Given I start diagnostics
        Then i receive a "question"
        When i input "n"
        Then i receive a "question"
        When i input "n"
        Then i receive a "question"
        When i input "y"
        Then i receive a "question"
        When i input "u"
        Then i receive a "warning"
        Then i receive a "question"
        When i input "y"
        Then i receive a "question"
        When i input "y"
        Then i receive a "Diagnosis:accident cerebrovascular"

    Scenario: You are healthy
        Given I start diagnostics
        Then i receive a "question"
        When i input "n"
        Then i receive a "question"
        When i input "n"
        Then i receive a "question"
        When i input "n"
        Then i receive a "question"
        When i input "n"
        Then i receive a "question"
        When i input "n"
        Then i receive a "question"
        When i input "n"
        Then i receive a "question"
        When i input "n"
        Then i receive a "question"
        When i input "n"
        Then i receive a "question"
        When i input "n"
        Then i receive a "question"
        When i input "n"
        Then i receive a "question"
        When i input "n"
        Then i receive a "question"
        When i input "n"
        Then i receive a "question"
        When i input "n"
        Then i receive a "question"
        When i input "n"
        Then i receive a "question"
        When i input "n"
        Then i receive a "question"
        When i input "n"
        Then i receive a "question"
        When i input "n"
        Then i receive a "question"
        When i input "n"
        Then i receive a "question"
        When i input "n"
        Then i receive a "question"
        When i input "n"
        Then i receive a "question"
        When i input "n"
        Then i receive a "question"
        When i input "n"
        Then i receive a "question"
        When i input "n"
        Then i receive a "You are healthy"