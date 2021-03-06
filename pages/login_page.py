from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "This is not URL for login"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True
		
    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.EMAIL)
        input_password = self.browser.find_element(*LoginPageLocators.PASSWORD)
        input_Confirm_password = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        input_email.send_keys(email)
        input_password.send_keys(password)
        input_Confirm_password.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        register_button.click()		