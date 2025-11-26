from playwright.sync_api import Page
from pages.login_page import LoginPage

def test_unsuccessful_authorization_with_invalid_data(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.fill_invalid_login_and_password()
    login_page.click_button()
    login_page.check_error_with_invalid_data()

def test_unsuccessful_authorization_with_unfilled_fields(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.click_button()
    login_page.check_error_with_unfilled_fields()