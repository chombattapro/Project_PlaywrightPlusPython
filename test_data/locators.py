class LoginPageLocators:
    username_input = "[data-test='username']"
    password_input = "[data-test='password']"
    login_button = "[data-test='login-button']"

    error_data = "[data-test='error']"

class InventoryPageLocators:
    product_card = "[data-test='inventory-item']"
    product_title = ".inventory_item_name[data-test='inventory-item-name']"  # Заголовок
    product_price = ".inventory_item_price[data-test='inventory-item-price']"  # Цена
    add_to_cart_button = "button[data-test^='add-to-cart-']"

    cart_button = "[data-test='shopping-cart-link']"
