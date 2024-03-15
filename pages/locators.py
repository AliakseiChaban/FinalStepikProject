from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM_ON_THE_LOGIN_PAGE = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM_ON_THE_LOGIN_PAGE = (By.CSS_SELECTOR, "#register_form1")


class ProductPageLocators:
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BASKET_VALUE = (By.CSS_SELECTOR, "div.basket-mini")
    SUCCESS_MESSAGE_WITH_PRODUCT_NAME = (By.CSS_SELECTOR, "div#messages div.alert:nth-child(1) div.alertinner ")
    SUCCESS_MESSAGE_WITH_BASKET_COST = (By.CSS_SELECTOR, "div#messages div.alert:nth-child(3)")


