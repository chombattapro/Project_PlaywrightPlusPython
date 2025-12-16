from playwright.sync_api import expect
from pages.base_page import BasePage, BASE_URL
from test_data.locators import InventoryPageLocators

class InventoryPage(BasePage):
    url = f"{BASE_URL}/inventory.html"

    def __init__(self, page):
        super().__init__(page)
        self.locators = InventoryPageLocators
        self.product_card = self.page.get_by_test_id(self.locators.product_card)
        self.product_title = self.page.get_by_test_id(self.locators.product_title)
        self.product_price = self.page.get_by_test_id(self.locators.product_price)
        self.add_to_cart_button = self.page.locator(self.locators.add_to_cart_button)
        self.cart_button = self.page.get_by_test_id(self.locators.cart_button)

    def verify_products_count(self, expected_count):
        expect(self.product_card).to_have_count(expected_count)

    def verify_product_card(self, card_index):
        """
        Берем конкретную карточку по индексу и проверяем элементы внутри этой карточки
        """
        product_card = self.product_card.nth(card_index)
        expect(product_card.locator(self.product_title)).to_be_visible()
        expect(product_card.locator(self.product_title)).to_be_enabled()
        expect(product_card.locator(self.product_price)).to_be_visible()
        expect(product_card.locator(self.add_to_cart_button)).to_be_visible()
        expect(product_card.locator(self.add_to_cart_button)).to_be_enabled()

    def click_cart_button(self):
        self.cart_button.click()

    def add_to_cart(self, card_index):
        self.product_card.nth(card_index).locator(self.add_to_cart_button).click()
