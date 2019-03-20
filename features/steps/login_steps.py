from behave import *


@given(u'I am on the Home page')
def step_impl(context):
    context.login_page.navigate("https://daaz.com")


@given(u'I click on the {link_name} link in the Home page')
def step_impl(context, link_name):
    if link_name == 'Login':
        context.login_page.click_login_link()
    elif link_name == 'JoinNow':
        context.login_page.click_join_now_link()


@when(u'I enter invalid {username} username')
def step_impl(context, username):
    context.login_page.enter_username(username)


@then(u'I enter invalid {password} password')
def step_impl(context, password):
    context.login_page.enter_password(password)


@then(u'I submit login details')
def step_impl(context):
    context.login_page.click_login_page_submit_button()


@then(u'I close the login popup')
def step_impl(context):
    context.login_page.click_login_close_button()


@then(u'I should see the registration page is opened in the same tab')
def step_impl(context):
    # assert_true(context.login_page.verify_registration_url())
    assert "/register" in context.login_page.verify_registration_url()
