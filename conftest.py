import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage

@pytest.fixture(scope="function")
def login(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.fill_valid_login_and_password()
    yield page
