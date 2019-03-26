from behave import given, when, then, use_step_matcher, register_type
import parse


@given(u'I am on the Home page')
def step_impl(context):
    context.login_page.navigate("https://daaz.com")


@given(u'I click on the {link_name} link in the Home page')
def step_impl(context, link_name):
    if link_name == 'Login':
        context.login_page.click_login_link()
    elif link_name == 'JoinNow':
        context.login_page.click_join_now_link()

# The below two methods for step_matcher
@parse.with_pattern(r"\S+")
def parse_string(text):
     return text.strip()


register_type(Name=parse_string)
use_step_matcher("cfparse")


@when(u'I enter invalid {key:Name*} username')
def step_impl(context, key):
    context.login_page.enter_username(key)


@then(u'I enter invalid {key:Name*} password')
def step_impl(context, key):
    context.login_page.enter_password(key)


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
