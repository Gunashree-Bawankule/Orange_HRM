from behave import *
from playwright.sync_api import expect

#from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage


@given("user is on the login page")
def step_impl(context):
    # context.playwright = sync_playwright().start()
    # context.browser = context.playwright.chromium.launch(headless=False)
    # context.page=context.browser.new_page()
    context.login_page = LoginPage(context.page)
    context.login_page.navigate()

@when("user enter valid {username} and {password}")
def step_impl(context, username, password):
    """
    :type context: behave.runner.Context
    :type username: str
    :type password: str
    """
    context.login_page.enter_credentials(username, password)


@when("user click on the login button")
def step_impl(context):
      context.login_page.click_login_button()
      context.page.wait_for_timeout(5000)

@then("user should be redirected to the dashboard")
def step_impl(context):
    assert context.page.url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

@then("the user should see an error message")
def step_impl(context):
    expect(context.page.get_by_text('Invalid credentials')).to_be_visible()


@When("the user enters invalid {invalid_username} and {invalid_password}")
def step_impl(context, invalid_username, invalid_password):
    """
    :type context: behave.runner.Context
    :type invalid_username: str
    :type invalid_password: str
    """
    context.login_page.enter_credentials(invalid_username, invalid_password)
