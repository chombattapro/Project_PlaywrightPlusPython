from playwright.sync_api import Page
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_the_full_cycle_of_successful_purchase(login, page: Page, faker):
    inventory_page = InventoryPage(login)
    inventory_page.add_to_cart(0)
    inventory_page.add_to_cart(1)
    inventory_page.add_to_cart(2)
    inventory_page.add_to_cart(3)
    inventory_page.verify_cart_button()
    cart_page = CartPage(page)
    cart_page.verify_checkout_button()
    cart_page.fill_in_user_details(faker)
    cart_page.verify_finish_button()
    cart_page.check_massage_about_a_successful_purchase()





