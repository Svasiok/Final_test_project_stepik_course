from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.XPATH, "//div[2]/div/div[2]/div[2]/div/div[2]/form/button")
    
	
class ProductPageLocators():
    PRODUCT_NAME = (By.XPATH, '//div[2]/div/div[1]/div[1]/div/strong')
    PRICE_PRODUCT = (By.XPATH, '//div[2]/div/div[1]/div[3]/div/p[1]/strong')
    BASKET_FORM = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_NAME_ADD = (By.XPATH, '//div[2]/div/div[2]/div[2]/article/div[1]/div[2]/h1')
    PRICE_PRODUCT_ADD = (By.XPATH, '//div[2]/div/div[2]/div[2]/article/div[1]/div[2]/p[1]')
    MESSAGE_SUCCESS = (By.XPATH, '//div[2]/div/div[1]/div[2]/div')
	
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.XPATH, '//header/div[1]/div/div[2]/span')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
	
class BasketPageLocators():
     BASKET_ITEM = (By.CSS_SELECTOR, "div.basket-items")
     BASKET_MESSAGE = (By.XPATH, '//div[2]/div/div[3]/div[2]/p/text()')