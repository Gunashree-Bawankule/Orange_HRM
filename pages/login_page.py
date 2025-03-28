# This file contains the login page object with methods for interacting with the login page.
from playwright.sync_api import Page


class LoginPage(Page):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.username_input = page.locator('//input[@name="username"]')
        self.password_input = page.locator('//input[@name="password"]')
        self.login_button = page.locator('//button[@type="submit"]')
        self.error_message = page.locator('//div[@role="alert"]')
        self.forgot_password_link = page.locator(
            '//p[@class="oxd-text oxd-text--p orangehrm-login-forgot-header"]'
        )

    def navigate_to_login_page(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com")

    def enter_credentials(self, username: str, password: str):
        self.username_input.press_sequentially(username, delay=400)
        self.password_input.press_sequentially(password, delay=400)

    def click_login_button(self):
        self.login_button.click()

    def is_logged_in(self):
        return (
            "dashboard"
            in self.page.url
            == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        )

    def get_error_message(self):
        return self.error_message.inner_text()

    # def click_forget_password_link(self):
    #     self.forgot_password_link.click()
