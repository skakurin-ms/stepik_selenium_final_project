from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_message_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_IS_EMPTY),\
            "Basket is empty message isn't presented"

    def should_be_no_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_LIST), \
            "Items are presented, but should not be"
