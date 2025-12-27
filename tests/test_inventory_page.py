import pytest
from pages.inventory_page import InventoryPage

@pytest.mark.inventory
@pytest.mark.smoke
def test_verify_products_count(login):
    inventory_page = InventoryPage(login)
    inventory_page.verify_products_count(6)

@pytest.mark.inventory
def test_verify_product_card_elements_and_cart_button(login):
    inventory_page = InventoryPage(login)
    inventory_page.verify_product_card(0)
