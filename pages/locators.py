from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_FORM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_FORM_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")

class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    MESSAGE_WITH_ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, ".alertinner > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    MESSAGE_WITH_ADDED_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alertinner > p > strong")
    PRODUCT_NAME_IN_TITLE = (By.CSS_SELECTOR, "h1")
    PRODUCT_PRICE_IN_TITLE = (By.CSS_SELECTOR, ".col-sm-6.product_main > .price_color")

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:
    MESSAGE_BASKET_IS_EMPTY = (By.CSS_SELECTOR, "div #content_inner")
    ITEMS_LIST = (By.CSS_SELECTOR, "div.basket-items")


