from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.BASKET_FORM)
        basket.click()
        
        
    def should_be_same_product_name(self):
         item_name_add = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ADD)
         item_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
         print(item_name.text)
         assert item_name.text == item_name_add.text, 'product name is not same'
         assert True
		 
    def should_be_same_price(self):
         price_add = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_ADD)
         price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)
         print(price.text)
         assert price.text == price_add.text, 'product price is not same'
         assert True