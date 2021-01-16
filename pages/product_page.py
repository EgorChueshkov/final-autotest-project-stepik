from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def should_be_success_messages(self):
        self.should_be_success_message_with_product_name()
        self.should_be_message_with_cost_of_the_basket()

    def should_be_success_message_with_product_name(self):
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert success_message == product_name, "Not a successful message about adding a product to the cart"

    def should_be_message_with_cost_of_the_basket(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE).text
        assert product_price == basket_total_price, "The cost of the basket does not match the price of the product"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"


