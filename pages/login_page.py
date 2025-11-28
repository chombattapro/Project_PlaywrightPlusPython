from playwright.sync_api import expect
from pages.base_page import BasePage
from configs.locators import LoginPageLocators
from configs.testdata import LoginPageData
from configs.urls import LoginPageResult

class LoginPage(BasePage):
    def fill_valid_login_and_password(self):
        self.page.locator(LoginPageLocators.username_input).fill(LoginPageData.valid_username)
        self.page.locator(LoginPageLocators.password_input).fill(LoginPageData.valid_password)
        self.page.locator(LoginPageLocators.login_button).click()
        expect(self.page).to_have_url(LoginPageResult.result_url)

    def fill_invalid_login_and_password(self):
        self.page.locator(LoginPageLocators.username_input).fill(LoginPageData.invalid_username)
        self.page.locator(LoginPageLocators.password_input).fill(LoginPageData.invalid_password)
        self.page.locator(LoginPageLocators.login_button).click()

    def check_error_with_invalid_data(self):
        result = self.page.locator(LoginPageLocators.error_invalid_data)
        expect(result).to_have_text(LoginPageData.error_invalid_data)

    def check_error_with_unfilled_fields(self):
        self.page.locator(LoginPageLocators.login_button).click()
        result = self.page.locator(LoginPageLocators.error_invalid_data)
        expect(result).to_have_text(LoginPageData.error_unfilled_fields)



