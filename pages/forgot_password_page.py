from playwright.sync_api import Page
class ForgotPasswordPage:
    def __init__(self, page: Page):
        self.page = page
        self.forgot_password_link = page.locator('//p[@class="oxd-text oxd-text--p orangehrm-login-forgot-header"]')
        self.username_input = page.locator('//input[@name="username"]')
        self.reset_password_button = page.locator('//button[@type="submit"]')
        self.message_input = page.locator('//input[@name="message"]')
        self.error_message = page.locator('//div[@role="alert"]')

    def navigate_to_login_page(self):
      self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def click_forgot_password_link(self):
        self.forgot_password_link.click()

    def enter_username(self, username: str):
        self.username_input.fill(username)

    def click_reset_password_button(self):
        self.reset_password_button.click()

    def get_message(self):
        return self.message.inner_text()

    def get_error_message(self):
        return self.error_message.inner_text()