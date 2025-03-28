from behave import when, then
from playwright.sync_api import sync_playwright


@when("user click on the forget password link")
def forget_password_link(context):
    context.page.click('text="Forgot your password?"')


@when("user enters the registered {username}")
def enter_registered_username(context, username):
    context.page.wait_for_selector('input[name="username"]', state="visible")
    context.page.fill('input[name="username"]', username)


@when('user click on the "Reset Password" button')
def reset_password(context):
    button_locator = context.page.locator("//button[@type='submit']")
    assert button_locator.is_visible(timeout=10), "Button was not found on page"
    context.page.goto(
        "https://opensource-demo.orangehrmlive.com/web/index.php/auth/sendPasswordReset"
    )


@then("user should see a confirmation message")
def confirmation_message(context):
    confirmation_message_locator = context.page.locator(
        "//h6[contains(@class, 'orangehrm-forgot-password-title')]"
    )
    confirmation_message_locator.wait_for(state="visible", timeout=5000)
    confirmation_message_text = confirmation_message_locator.text_content()
    assert "Reset Password link sent successfully" in confirmation_message_text.strip()
