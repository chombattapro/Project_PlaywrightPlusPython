from playwright.sync_api import expect
from pages.base_page import BasePage, BASE_URL
from test_data.locators import InventoryPageLocators

class InventoryPage(BasePage):
    url = f"{BASE_URL}/inventory.html"

    def __init__(self, page):
        super().__init__(page)
        self.locators = InventoryPageLocators

    @property
    def product_card(self):
        return self.page.get_by_test_id(self.locators.product_card)

    def verify_products_count(self, expected_count):
        product_card_counter = self.product_card
        expect(product_card_counter).to_have_count(expected_count)

    def verify_product_card(self, card_index):
        """
        Берем конкретную карточку по индексу и проверяем элементы внутри этой карточки
        """
        product_card = self.product_card.nth(card_index)
        title = product_card.locator(self.locators.product_title)
        expect(title).to_be_visible()
        expect(title).to_be_enabled()
        price = product_card.locator(self.locators.product_price)
        expect(price).to_be_visible()
        add_to_cart_button = product_card.locator(self.locators.add_to_cart_button)
        expect(add_to_cart_button).to_be_visible()
        expect(add_to_cart_button).to_be_enabled()

    def click_cart_button(self):
        self.page.get_by_test_id(self.locators.cart_button).click()

    def add_to_cart(self, card_index):
        product_card = self.product_card.nth(card_index)
        product_card.locator(self.locators.add_to_cart_button).click()
