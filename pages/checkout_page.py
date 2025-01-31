# pages/cart_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):

    # Locators
    TITLE = (By.XPATH, "//h2[.='Address Details']")
    YOUR_DELIVERY_ADDRESS_TITLE = (By.XPATH, "//*[@id='address_delivery']/li[1]/h3")
    YOUR_DELIVERY_ADDRESS_NAME = (By.XPATH, "//*[@id='address_delivery']/li[2]")
    YOUR_DELIVERY_ADDRESS_ADDRESS = (By.XPATH, "//*[@id='address_delivery']/li[3]")
    YOUR_DELIVERY_ADDRESS_CITY_STATE_ZIP = (By.XPATH, "//*[@id='address_delivery']/li[6]")
    YOUR_DELIVERY_ADDRESS_COUNTRY = (By.XPATH, "//ul[@id='address_delivery']/li[@class='address_country_name']")
    YOUR_DELIVERY_ADDRESS_PHONE = (By.XPATH, "//ul[@id='address_delivery']/li[@class='address_phone']")
    PRODUCTS_LIST_TABLE = (By.XPATH, "//*[@id='cart_info']")
    PLACE_ORDER_BTN = (By.XPATH, "//a[.='Place Order']")

    # Initialize the class
    def __init__(self, browser):
        super().__init__(browser)
        self.browser.get('https://automationexercise.com/checkout')
        self.wait_for_page_load()

    