from playwright.sync_api import expect
from pages.base_page import BasePage
from test_data.locators import InventoryPageLocators


class InventoryPage(BasePage):
    url = f"{BasePage.base_url}/inventory.html"

    def verify_products_count(self, expected_count):
        product = self.page.locator(InventoryPageLocators.product)
        expect(product).to_have_count(expected_count)

    def verify_first_product_elements(self):
        title = self.page.locator(InventoryPageLocators.product_title_first)
        expect(title).to_be_visible()
        expect(title).to_be_enabled()
        price = self.page.locator(InventoryPageLocators.product_price_first).first
        expect(price).to_be_visible()
        add_to_cart_button = self.page.locator(InventoryPageLocators.product_btn_add_to_cart_first)
        expect(add_to_cart_button).to_be_visible()
        expect(add_to_cart_button).to_be_enabled()

    def verify_cart_button(self):
        cart_button = self.page.locator(InventoryPageLocators.cart_button)
        expect(cart_button).to_be_visible()
        expect(cart_button).to_be_enabled()