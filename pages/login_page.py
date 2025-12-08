from playwright.sync_api import expect
from pages.base_page import BasePage
from test_data.locators import LoginPageLocators
from test_data.credentials import LoginPageData
from test_data.error_messages import LoginPageErrors

class LoginPage(BasePage):
    def fill_valid_login_and_password(self):
        self.page.locator(LoginPageLocators.username_input).fill(LoginPageData.valid_username)
        self.page.locator(LoginPageLocators.password_input).fill(LoginPageData.valid_password)
        self.page.locator(LoginPageLocators.login_button).click()
        expect(self.page).to_have_url(f"{BasePage.base_url}/inventory.html")

    def fill_invalid_login_and_password(self):
        self.page.locator(LoginPageLocators.username_input).fill(LoginPageData.invalid_username)
        self.page.locator(LoginPageLocators.password_input).fill(LoginPageData.invalid_password)
        self.page.locator(LoginPageLocators.login_button).click()

    def check_error_with_invalid_data(self):
        error_message1 = self.page.locator(LoginPageLocators.error_data)
        expect(error_message1).to_have_text(LoginPageErrors.error_invalid_data)

    def check_error_with_unfilled_fields(self):
        self.page.locator(LoginPageLocators.login_button).click()
        error_message2 = self.page.locator(LoginPageLocators.error_data)
        expect(error_message2).to_have_text(LoginPageErrors.error_unfilled_fields)

