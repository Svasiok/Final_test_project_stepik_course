from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
	
class ProductPageLocators():
    PRODUCT_NAME = (By.XPATH, '//div[2]/div/div[1]/div[1]/div/strong')
    PRICE_PRODUCT = (By.XPATH, '//div[2]/div/div[1]/div[3]/div/p[1]/strong')
    BASKET_FORM = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_NAME_ADD = (By.XPATH, '//div[2]/div/div[2]/div[2]/article/div[1]/div[2]/h1')
    PRICE_PRODUCT_ADD = (By.XPATH, '//div[2]/div/div[2]/div[2]/article/div[1]/div[2]/p[1]')