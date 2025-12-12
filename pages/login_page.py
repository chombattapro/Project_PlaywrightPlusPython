from playwright.sync_api import expect
from pages.base_page import BasePage, BASE_URL
from test_data.locators import LoginPageLocators
from test_data.credentials import LoginPageData
from test_data.error_messages import LoginPageErrors

class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.locators = LoginPageLocators
        self.data = LoginPageData
        self.errors = LoginPageErrors

    @property
    def username_input(self):
        return self.page.get_by_test_id(self.locators.username_input)

    @property
    def password_input(self):
        return self.page.get_by_test_id(self.locators.password_input)

    @property
    def error_data(self):
        return self.page.get_by_test_id(self.locators.error_data)

    def fill_valid_login_and_password(self):
        self.username_input.fill(self.data.valid_username)
        self.password_input.fill(self.data.valid_password)
        self.page.get_by_test_id(self.locators.login_button).click()
        expect(self.page).to_have_url(f"{BASE_URL}/inventory.html")

    def fill_invalid_login_and_password(self):
        self.username_input.fill(self.data.invalid_username)
        self.password_input.fill(self.data.invalid_password)
        self.page.get_by_test_id(self.locators.login_button).click()

    def check_error_with_invalid_data(self):
        error_message1 = self.error_data
        expect(error_message1).to_have_text(self.errors.error_invalid_data)

    def check_error_with_unfilled_fields(self):
        self.page.get_by_test_id(self.locators.login_button).click()
        error_message2 = self.error_data
        expect(error_message2).to_have_text(self.errors.error_unfilled_fields)

