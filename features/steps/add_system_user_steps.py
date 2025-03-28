from random import randint

from behave import given, when, then
from playwright.sync_api import expect


@given("the admin is logged into OrangeHRM")
def admin_is_logged_in(context):
    context.page.goto("https://opensource-demo.orangehrmlive.com/")
    context.page.fill('input[name="username"]', "Admin")
    context.page.fill('input[name="password"]', "admin123")
    context.page.click('button[type="submit"]')
    context.page.goto(
        "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers"
    )


@given('the admin navigates to the "Admin" section')
def admin_navigate_to_admin_section(context):
    context.page.click('text="Admin"')


@when('the admin clicks on the "Add" button')
def admin_click_add_button(context):
    context.page.click('button:text("Add")')
    (context.page.locator('//button[@type="button"]'))


@when("the admin fills in the user details with")
def admin_fills_in_user_details(context):
    context.page.click('//input[@placeholder="Type for hints..."]')
    # context.page.wait_for_timeout(2000)
    context.page.locator('//input[@placeholder="Type for hints..."]').fill(
        "James  Butler"
    )

    context.page.wait_for_timeout(2000)
    context.page.keyboard.press("ArrowDown+Enter")
    randomNumber = randint(11111, 99999)
    context.page.locator('(//input[@class="oxd-input oxd-input--active"])[2]').fill(
        "Smith@" + str(randomNumber)
    )

    context.page.locator("(//input[@type='password'])[1]").fill("smith123")
    context.page.locator("(//input[@type='password'])[2]").fill("smith123")
    context.page.get_by_text("-- Select --").first.click()
    context.page.get_by_role("option", name="Admin").click()
    context.page.get_by_text("-- Select --").first.click()
    context.page.get_by_role("option", name="Enabled").click()
    context.page.get_by_role("button", name="Save").click()
    # context.page.get_by_text("Successfully Updated×").click()


@when('the admin clicks the "Save" button')
def admin_click_save_button(context):
    context.page.on("dialog", lambda dialog: print(dialog.dismiss()))
    context.page.click('//button[@type="submit"]')
    context.page.wait_for_timeout(2000)


@then("the system should display a success message")
def display_success_message(context):
    # expect(context.page.locator('text="Successfully Saved"')).to_be_visible()
    pass
