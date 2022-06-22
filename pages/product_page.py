from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.BASKET_FORM)
        basket.click()
        
        
    def should_be_same_product_name(self):
         item_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
         print(item_name.text)
         assert item_name.text == "The shellcoder's handbook", 'product name is not same'
         assert True
		 
    def should_be_same_price(self):
         price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)
         print(price.text)
         assert price.text == "£9.99", 'product price is not same'
         assert True