from behave import *
from inspection import inspection

@given('we have behave installed')
def step_diagnostics(context):
    context.game_inst = inspection()

@when('input "{yn}"')
def step_input(context, yn):
    context.game_inst.ans_setter(yn)
    assert not(context.game_inst.context.ans_check())
    assert (len(context.game_inst.ddb_getter().columns) > 1
            and len(context.game_inst.ddb_getter()) > 1)

@then('Then i receive a "{expected_output}"')
def step_out(context, expected_output):
    if expected_output == 'question':
        context.game_inst.context.question()
        assert not(context.game_inst.context.ans_check())
    if expected_output == 'warning':
        assert context.game_inst.context.ans_check()
    else:
        assert not(len(context.game_inst.ddb_getter().columns) > 1
                and len(context.game_inst.ddb_getter()) > 1)
        assert context.game_inst.final() == expected_output