# pages/cart_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PaymentPage(BasePage):

    # Locators
    TITLE = (By.XPATH, "//h2[@class='heading']") #PAYMENT 
    NAME_ON_CARD_INPUT_FIELD = (By.XPATH, "//input[@name='name_on_card']")
    CARD_NUMBER_INPUT_FIELD = (By.XPATH, "//input[@name='card_number']")
    CVC_CODE_INPUT_FIELD = (By.XPATH, "//input[@name='cvc']")
    EXPIRATION_MONTH_INPUT_FIELD = (By.XPATH, "//input[@name='expiry_month']")
    EXPIRATION_YEAR_INPUT_FIELD = (By.XPATH, "//input[@name='expiry_year']")
    PAY_NOW_BTN = (By.XPATH, "//button[@id='submit']")

    # Initialize the class
    def __init__(self, browser):
        super().__init__(browser)
        self.browser.get('https://automationexercise.com/payment')
        self.wait_for_page_load()

    