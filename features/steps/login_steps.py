from behave import given, when, then
from playwright.sync_api import expect
from pages.login_page import LoginPage


@given("user is on the login page")
def open_login_page(context):
    context.login_page = LoginPage(context.page)
    context.login_page.navigate_to_login_page()
    context.page.goto("https://opensource-demo.orangehrmlive.com/")


@when("user enter valid {username} and {password}")
def enter_valid_credentials(context, username, password):
    context.login_page.enter_credentials(username, password)


@when("the user enters invalid {invalid_username} and {invalid_password}")
def enter_credentials(context, invalid_username, invalid_password):
    print(f"Invalid Username: {invalid_username}, Invalid Password: {invalid_password}")
    context.login_page.enter_credentials(invalid_username, invalid_password)


@when("user click on the login button")
def click_login_button(context):
    context.login_page.click_login_button()
    context.page.wait_for_timeout(5000)


@then("user should be redirected to the dashboard")
def verify_dashboard(context):
    current_url = context.login_page.url
    assert (
        current_url
        == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    )


@then("the user should see an error message")
def error_message(context):
    expect(context.login_page.get_by_text("Invalid credentials")).to_be_visible()
