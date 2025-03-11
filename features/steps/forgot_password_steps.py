from behave import *
from playwright.sync_api import sync_playwright, expect
from pages.forgot_password_page import ForgotPasswordPage


def before_scenario(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)
    context.page = context.browser.new_page()
    context.forgot_password_page = ForgotPasswordPage(context.page)

def after_scenario(context, scenario):
  pass

@when('user click on the "Forgot your password?" link')
def step_impl(context):
    context.forgot_password_page.click_forgot_password_link()

@when('user enter the registered {username} "user"')
def step_impl(context, username):
    context.forgot_password_page.enter_username(username)

@when('user click on the "Reset Password" button')
def step_impl(context):
    context.forgot_password_page.click_reset_password_button()

@then('user should see a confirmation message "Reset Password link sent successfully."')
def step_impl(context, message):
    context.forgot_password_page.check_confirmation_message()

