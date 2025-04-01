from random import randint

from behave import given, when, then
from pages.login_page import LoginPage


@given("user logged into the OrangeHRM")
def login_page(context):
    context.login_page = LoginPage(context.page)
    context.login_page.navigate_to_login_page()
    context.page.goto("https://opensource-demo.orangehrmlive.com/")
    context.login_page.enter_credentials("Admin", "admin123")
    context.login_page.click_login_button()


@when("user navigates to the admin page")
def navigates_to_admin_page(context):
    from pages.Admin_page import AdminPage

    context.admin_page = AdminPage(context.page)
    context.admin_page.navigate_to_admin_page()


@when('user added a new user with {employee_name} "John Doe" {user_role} "admin"')
def step_impl(context, employee_name, user_role):
    result = context.admin_page.enter_credentials(employee_name, user_role)
    context.page.wait_for_timeout(2000)
    context.page.keyboard.press("ArrowDown+Enter")
    randomNumber = randint(11111, 99999)
    context.page.locator("//input[@placeholder='Type for hints...']").fill(
        "John Doe" + str(randomNumber)
    )
    context.page.locator('//button[@type="submit"]').click()
    return result, "User was not added"


@then('the user "John Doe" should be created successfully')
def step_impl(context):
    pass
