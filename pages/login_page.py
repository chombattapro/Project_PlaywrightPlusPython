from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.locators import LoginPageLocators

class LoginPage(BasePage):
    url = "https://saucedemo.com"
    result_url = "https://www.saucedemo.com/inventory.html"

    valid_username = "standard_user"
    valid_password = "secret_sauce"

    invalid_username = "p_user"
    invalid_password = "p_sauce"

    def fill_valid_login_and_password(self):
        self.page.locator(LoginPageLocators.username_input).fill(self.valid_username)
        self.page.locator(LoginPageLocators.password_input).fill(self.valid_password)

    def fill_invalid_login_and_password(self):
        self.page.locator(LoginPageLocators.username_input).fill(self.invalid_username)
        self.page.locator(LoginPageLocators.password_input).fill(self.invalid_password)

    def click_button(self):
        self.page.locator(LoginPageLocators.login_button).click()

    def check_result_url(self):
        expect(self.page).to_have_url(self.result_url)

    def check_error_with_invalid_data(self):
        result = self.page.locator(LoginPageLocators.error_invalid_data)
        expect(result).to_have_text("Epic sadface: Username and password do not match any user in this service")

    def check_error_with_unfilled_fields(self):
        result = self.page.locator(LoginPageLocators.error_invalid_data)
        expect(result).to_have_text("Epic sadface: Username is required")



