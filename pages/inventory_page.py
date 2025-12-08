from playwright.sync_api import expect
from pages.base_page import BasePage
from test_data.locators import InventoryPageLocators


class InventoryPage(BasePage):
    url = f"{BasePage.base_url}/inventory.html"

    def verify_products_count(self, expected_count):
        product_card_counter = self.page.locator(InventoryPageLocators.product_card)
        expect(product_card_counter).to_have_count(expected_count)

    def verify_product_card(self, card_index):
        """
        Берем конкретную карточку по индексу и проверяем элементы внутри этой карточки
        """
        product_card = self.page.locator(InventoryPageLocators.product_card).nth(card_index)
        title = product_card.locator(InventoryPageLocators.product_title)
        expect(title).to_be_visible()
        expect(title).to_be_enabled()
        price = product_card.locator(InventoryPageLocators.product_price)
        expect(price).to_be_visible()
        add_to_cart_button = product_card.locator(InventoryPageLocators.add_to_cart_button)
        expect(add_to_cart_button).to_be_visible()
        expect(add_to_cart_button).to_be_enabled()

    def verify_cart_button(self):
        cart_button = self.page.locator(InventoryPageLocators.cart_button)
        expect(cart_button).to_be_visible()
        expect(cart_button).to_be_enabled()
        cart_button.click()

    def add_to_cart(self, card_index):
        product_card = self.page.locator(InventoryPageLocators.product_card).nth(card_index)
        expect(product_card).to_be_visible()
        expect(product_card).to_be_enabled()
        product_card.locator(InventoryPageLocators.add_to_cart_button).click()
