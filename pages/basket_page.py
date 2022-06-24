from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from .locators import BasketPageLocators
from .locators import BasePageLocators

class BasketPage(BasePage):
    def should_not_be_product(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), 'No empty basket'
        assert True
		
    def should_be_text_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_MESSAGE), 'Message - Your basket no empty'
        assert True