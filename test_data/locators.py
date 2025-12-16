class LoginPageLocators:
    username_input = "username"
    password_input = "password"
    login_button = "login-button"

    error_data = "error"

class InventoryPageLocators:
    product_card = "inventory-item"
    product_title = "inventory-item-name"  # Заголовок
    product_price = "inventory-item-price"  # Цена
    add_to_cart_button = "button[data-test^='add-to-cart-']"

    cart_button = "shopping-cart-link"

class CartPageLocators:
    product_card_in_cart = "inventory-item"
    checkout_button = "checkout"

    first_name = "firstName"
    last_name = "lastName"
    postal_code = "postalCode"

    continue_button = "continue"

    finish_button = "finish"

    successful_purchase_message = "complete-header"
    back_home_button = "back-to-products"
