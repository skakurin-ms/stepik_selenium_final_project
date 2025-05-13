from .base_page import BasePage
from .locators import ProductPageLocators

from time import sleep

class ProductPage(BasePage):
    def add_product_to_basket(self):
        # self.should_be_promo_url()
        # self.should_be_add_to_basket_button()

        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

        # self.solve_quiz_and_get_code()
        # self.should_be_message_with_added_product_name()
        # self.should_be_correct_product_name()
        # self.should_be_message_with_added_product_price()
        # self.should_be_correct_product_price()

    def should_be_promo_url(self):
        assert "?promo=" in self.browser.current_url, f"Parameter 'promo=newYear' is absent in {self.url}"

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON),\
            "Add to basket button isn't presented"

    def should_be_message_with_added_product_name(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_WITH_ADDED_PRODUCT_NAME),\
            "Message with added product name isn't presented"

    def should_be_message_with_added_product_price(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_WITH_ADDED_PRODUCT_PRICE),\
            "Message with added product price isn't presented"

    def should_be_correct_product_name(self):
        product_name_in_title = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_TITLE).text
        product_name_in_message = self.browser.find_element(
            *ProductPageLocators.MESSAGE_WITH_ADDED_PRODUCT_NAME).text
        print("NAME in title:", product_name_in_title)
        print("NAME in message:", product_name_in_message)

        assert product_name_in_title == product_name_in_message,\
            f"Product name isn't correct: {product_name_in_message} instead of {product_name_in_title}"

    def should_be_correct_product_price(self):
        product_price_in_title = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_TITLE).text
        product_price_in_message = self.browser.find_element(
            *ProductPageLocators.MESSAGE_WITH_ADDED_PRODUCT_PRICE).text
        assert product_price_in_title == product_price_in_message,\
            f"Product price isn't correct: {product_price_in_message} instead of {product_price_in_title}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_WITH_ADDED_PRODUCT_NAME),\
            "Success message is presented, but should not be"

    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_WITH_ADDED_PRODUCT_NAME),\
            "Success message isn't disappeared"

