from behave import *
from sympy import false

from inspection import inspection

@given('I start diagnostics')
def step_diagnostics(context):
    context.game_inst = inspection()
    context.flag = True

@when('i input "{yn}"')
def step_input(context, yn):
    context.game_inst.ans_setter(yn)
    assert (len(context.game_inst.ddb_getter().columns) > 1
            and len(context.game_inst.ddb_getter()) > 1)
    context.flag = not(context.game_inst.ans_check())

@then('i receive a "{expected_output}"')
def step_out(context, expected_output):
    if expected_output == 'question':
        assert context.flag
        context.game_inst.question()
    elif expected_output == 'warning':
        context.flag = True
        assert context.game_inst.ans_check()
    else:
        assert not(len(context.game_inst.ddb_getter().columns) > 1 and len(context.game_inst.ddb_getter()) > 1)
        assert context.game_inst.final() == expected_output