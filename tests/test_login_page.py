from playwright.sync_api import Page
from pages.login_page import LoginPage

def test_successful_authorization_with_valid_data(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.fill_valid_login_and_password()



