from selenium.webdriver.common.by import By


class MainPageLocators:
    pass
    # LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.CSS_SELECTOR, "span.btn-group a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM_ON_THE_LOGIN_PAGE = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM_ON_THE_LOGIN_PAGE = (By.CSS_SELECTOR, "#register_form")

    REGISTER_EMAIL_ADDRESS_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PWD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PWD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BTN = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BASKET_VALUE = (By.CSS_SELECTOR, "div.basket-mini")
    SUCCESS_MESSAGE_WITH_PRODUCT_NAME = (By.CSS_SELECTOR, "div#messages div.alert:nth-child(1) div.alertinner ")
    SUCCESS_MESSAGE_WITH_BASKET_COST = (By.CSS_SELECTOR, "div#messages div.alert:nth-child(3)")


class BasketPageLocators:
    BASKET_IS_EMPTY_MESSAGE = (By.CSS_SELECTOR, "div#content_inner p")
    PRODUCT_IS_ADDED_TO_BASKET = (By.CSS_SELECTOR, "div.basket-items")
