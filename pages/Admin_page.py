from playwright.sync_api import Page


class AdminPage(Page):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.login_button = page.locator('//button[@type="submit"]')
        self.user_role_input = page.locator(
            "//label[text()='User Role']/parent::div/following-sibling::div//*[text()='-- Select --']"
        )
        self.employee_name_input = page.locator(
            "//input[@placeholder='Type for hints...']"
        )
        self.search_button = page.locator('//button[@type="submit"]')
        self.record_found = page.locator('//span[@class="oxd-text oxd-text--span"]')

    def navigate_to_admin_page(self):
        self.page.goto(
            "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers"
        )

    def enter_credentials(self, user_role="Admin", employee_name="John Doe Test"):
        self.page.get_by_text("-- Select --").first.click()
        self.page.get_by_role("option", name="Admin").click()

        self.page.wait_for_selector("input[placeholder='Type for hints...']")
        employee_name_input = self.page.locator(
            "//input[@placeholder='Type for hints...']"
        )
        assert employee_name_input.is_visible()
        employee_name_input.fill(employee_name)
        assert employee_name_input.input_value() == employee_name

        self.click_search_button()
        return True

    def click_search_button(self):
        self.search_button.click()

    def record_found(self):
        self.record_found.click()
