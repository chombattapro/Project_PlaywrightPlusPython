from playwright.sync_api import expect
from pages.base_page import BasePage
from test_data.locators import CartPageLocators

class CartPage(BasePage):
    url = f"{BasePage.base_url}/cart.html"

    def verify_checkout_button(self):
        checkout_button = self.page.locator(CartPageLocators.checkout_button)
        expect(checkout_button).to_be_visible()
        expect(checkout_button).to_be_enabled()
        checkout_button.click()

    def fill_in_user_details(self, faker):
        self.page.locator(CartPageLocators.first_name).fill(faker.first_name())
        self.page.locator(CartPageLocators.last_name).fill(faker.last_name())
        self.page.locator(CartPageLocators.postal_code).fill(faker.postcode())
        continue_button = self.page.locator(CartPageLocators.continue_button)
        expect(continue_button).to_be_visible()
        expect(continue_button).to_be_enabled()
        continue_button.click()

    def verify_finish_button(self):
        finish_button = self.page.locator(CartPageLocators.finish_button)
        expect(finish_button).to_be_visible()
        expect(finish_button).to_be_enabled()
        finish_button.click()

    def check_massage_about_a_successful_purchase(self):
        successful_massage = self.page.locator(CartPageLocators.successful_purchase_message)
        expect(successful_massage).to_be_visible()
        expect(successful_massage).to_contain_text("Thank you for your order!")
        back_home_button = self.page.locator(CartPageLocators.back_home_button)
        expect(back_home_button).to_be_visible()
        expect(back_home_button).to_be_enabled()
        back_home_button.click()