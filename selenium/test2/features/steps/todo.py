from behave import given, when, then

@given('que eu esteja na página')
def go_to_page(context):
    ...

@when('criar um todo')
def create_todo(context):
    ...

@then('o todo deve estar na pilha "{pilha}"')
def check_todo(context, pilha):
    ...