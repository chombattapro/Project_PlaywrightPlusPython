from playwright.sync_api import Page
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_verify_successful_purchase(login, page: Page):
    inventory_page = InventoryPage(login)
    products = [0, 1, 2, 3]
    for index in products:
        inventory_page.add_to_cart(index)
    inventory_page.click_cart_button()
    cart_page = CartPage(page)
    cart_page.verify_products_count_in_cart(len(products))
    cart_page.fill_in_user_details()
    cart_page.verify_products_count_in_final_checkout(len(products))
    cart_page.verify_message_about_a_successful_purchase()
