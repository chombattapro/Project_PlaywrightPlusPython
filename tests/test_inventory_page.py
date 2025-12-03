from pages.inventory_page import InventoryPage

def test_verify_products_count_after_login(login):
    inventory_page = InventoryPage(login)
    inventory_page.verify_products_count(6)

def test_verify_first_product_elements_after_login(login):
    inventory_page = InventoryPage(login)
    inventory_page.verify_first_product_elements()

def test_verify_cart_button_after_login(login):
    inventory_page = InventoryPage(login)
    inventory_page.verify_cart_button()