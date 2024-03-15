from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url_login_part = "login"
        assert url_login_part in self.browser.current_url, f"It's not the login page, check url contains '{url_login_part}'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_ON_THE_LOGIN_PAGE), "Log In form isn't found"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM_ON_THE_LOGIN_PAGE), \
            "Registration form isn't found"
