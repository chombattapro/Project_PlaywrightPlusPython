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

    @property
    def first_name(self):
        return self.page.get_by_test_id(self.locators.first_name)

    @property
    def last_name(self):
        return self.page.get_by_test_id(self.locators.last_name)

    @property
    def postal_code(self):
        return self.page.get_by_test_id(self.locators.postal_code)

    @property
    def product_card(self):
        return self.page.get_by_test_id(self.locators.product_card_in_cart)

    def verify_products_count_in_cart(self, expected_count):
        product_card_counter = self.product_card
        expect(product_card_counter).to_have_count(expected_count)
        self.page.get_by_test_id(self.locators.checkout_button).click()

    def fill_in_user_details(self):
        self.first_name.fill(fake.first_name())
        self.last_name.fill(fake.last_name())
        self.postal_code.fill(fake.postcode())
        self.page.get_by_test_id(self.locators.continue_button).click()

    def verify_products_count_in_final_checkout(self, expected_count):
        product_card_counter = self.product_card
        expect(product_card_counter).to_have_count(expected_count)
        self.page.get_by_test_id(self.locators.finish_button).click()

    def verify_message_about_a_successful_purchase(self):
        successful_massage = self.page.get_by_test_id(self.locators.successful_purchase_message)
        expect(successful_massage).to_be_visible()
        expect(successful_massage).to_contain_text("Thank you for your order!")
