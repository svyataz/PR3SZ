Feature: inspection

    Scenario: Diagnosis:accident cerebrovascular with miss input
        Given I start diagnostics
        Then i receive a question
        When input "n"
        Then i receive a question
        When input "n"
        Then i receive a question
        When input "y"
        Then i receive a question
        When input "u"
        Then i receive a warning
        Then i receive a question
        When input "y"
        Then i receive a question
        When input "y"
        Then i receive a Diagnosis:accident cerebrovascular