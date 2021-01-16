from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form > button.btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner > strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > p")
    BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, ".alert-info strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

