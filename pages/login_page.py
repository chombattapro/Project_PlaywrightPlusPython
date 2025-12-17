from playwright.sync_api import expect
from pages.base_page import BasePage, BASE_URL
from test_data.locators import LoginPageLocators
from test_data.credentials import LoginPageData
from test_data.error_messages import LoginPageErrors

class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.locators = LoginPageLocators
        self.username_input = self.page.get_by_test_id(self.locators.username_input)
        self.password_input = self.page.get_by_test_id(self.locators.password_input)
        self.login_button = self.page.get_by_test_id(self.locators.login_button)
        self.error_data = self.page.get_by_test_id(self.locators.error_data)
        self.data = LoginPageData
        self.valid_username = self.data.valid_username
        self.valid_password = self.data.valid_password
        self.invalid_username = self.data.invalid_username
        self.invalid_password = self.data.invalid_password
        self.errors = LoginPageErrors
        self.error_invalid_data = self.errors.error_invalid_data
        self.error_unfilled_fields = self.errors.error_unfilled_fields

    def fill_valid_login_and_password(self):
        self.username_input.fill(self.valid_username)
        self.password_input.fill(self.valid_password)
        self.login_button.click()
        expect(self.page).to_have_url(f"{BASE_URL}/inventory.html")

    def fill_invalid_login_and_password(self):
        self.username_input.fill(self.invalid_username)
        self.password_input.fill(self.invalid_password)
        self.login_button.click()

    def check_error_with_invalid_data(self):
        expect(self.error_data).to_have_text(self.error_invalid_data)

    def check_error_with_unfilled_fields(self):
        self.login_button.click()
        expect(self.error_data).to_have_text(self.error_unfilled_fields)

