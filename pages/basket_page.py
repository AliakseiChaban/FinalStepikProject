from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def is_basket_empty_message_present(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE), \
            "The Basket isn't empty or the message doesn't exist"

    def is_basket_contains_product(self):
        assert not self.is_element_present(*BasketPageLocators.PRODUCT_IS_ADDED_TO_BASKET), \
            "There shouldn't be added products"
