from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    MESSAGE_WITH_ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, ".alertinner > strong")
    MESSAGE_WITH_ADDED_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alertinner > p > strong")
    PRODUCT_NAME_IN_TITLE = (By.CSS_SELECTOR, "h1")
    PRODUCT_PRICE_IN_TITLE = (By.CSS_SELECTOR, ".col-sm-6.product_main > .price_color")
