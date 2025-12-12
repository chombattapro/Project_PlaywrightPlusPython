import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from faker import Faker

@pytest.fixture(scope="session", autouse=True)
def configure_test_selectors(playwright):
    playwright.selectors.set_test_id_attribute("data-test")

@pytest.fixture(scope="function")
def faker():
    return Faker()

@pytest.fixture(scope="function")
def login(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.fill_valid_login_and_password()
    yield page
