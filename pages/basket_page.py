from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_text_that_basket_is_empty(self):
        basket_text = self.browser.find_element(*BasketPageLocators.BASKET_TEXT).text
        assert 'Your basket is empty.' in basket_text, 'Not message that basket is empty'

    def should_not_be_products_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCT), 'Product in the basket, but should not be'

