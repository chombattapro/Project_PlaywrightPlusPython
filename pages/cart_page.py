from playwright.sync_api import expect
from pages.base_page import BasePage, BASE_URL
from test_data.locators import CartPageLocators
from faker import Faker

fake = Faker()

class CartPage(BasePage):
    url = f"{BASE_URL}/cart.html"

    def __init__(self, page):
        super().__init__(page)
        self.locators = CartPageLocators
        self.product_card_in_cart = self.page.get_by_test_id(self.locators.product_card_in_cart)
        self.checkout_button = self.page.get_by_test_id(self.locators.checkout_button)
        self.first_name = self.page.get_by_test_id(self.locators.first_name)
        self.last_name = self.page.get_by_test_id(self.locators.last_name)
        self.postal_code = self.page.get_by_test_id(self.locators.postal_code)
        self.continue_button = self.page.get_by_test_id(self.locators.continue_button)
        self.finish_button = self.page.get_by_test_id(self.locators.finish_button)
        self.successful_massage = self.page.get_by_test_id(self.locators.successful_purchase_message)

    def verify_products_count_in_cart(self, expected_count):
        expect(self.product_card_in_cart).to_have_count(expected_count)
        self.checkout_button.click()

    def fill_in_user_details(self):
        self.first_name.fill(fake.first_name())
        self.last_name.fill(fake.last_name())
        self.postal_code.fill(fake.postcode())
        self.continue_button.click()

    def verify_products_count_in_final_checkout(self, expected_count):
        expect(self.product_card_in_cart).to_have_count(expected_count)
        self.finish_button.click()

    def verify_message_about_a_successful_purchase(self):
        expect(self.successful_massage).to_be_visible()
        expect(self.successful_massage).to_contain_text("Thank you for your order!")
