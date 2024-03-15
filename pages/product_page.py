import time

from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN).click()

    def is_successful_message_contains_added_product_name(self):

        product_name_text = self.get_elements_text(*ProductPageLocators.PRODUCT_NAME)
        expected_success_message_text = self.get_elements_text(*ProductPageLocators.SUCCESS_MESSAGE_WITH_PRODUCT_NAME)

        current_success_message_text = f"{product_name_text.lower()} has been added to your basket."

        assert current_success_message_text.lower() == expected_success_message_text.lower(), \
            f"The SUCCESS_MESSAGE has to be {expected_success_message_text} instead of " \
            f"{current_success_message_text}, check the product name or the message body"

    def is_total_cost_message_present(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE_WITH_BASKET_COST),\
            "There is no total cost message"

    def is_basket_price_equals_to_added_product_price(self):
        product_price_text = self.get_elements_text(*ProductPageLocators.PRODUCT_PRICE)
        basket_price_text = self.get_elements_text(*ProductPageLocators.BASKET_VALUE)

        assert product_price_text in basket_price_text, f"The cost in the Basket has to be {product_price_text}"
