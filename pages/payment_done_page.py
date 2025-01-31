from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class PaymentDonePage(BasePage):

    # Locators
    TITLE = (By.XPATH, "//b[.='Order Placed!']") # ORDER PLACED! 
    CONFIRMATION_TEXT = (By.XPATH, "//p[.='Congratulations! Your order has been confirmed!']")
    DOWNLOAD__INVOICE_BTN = (By.XPATH, "//a[.='Download Invoice']")
    CONTINUE_BTN = (By.XPATH, "//a[.='Continue']")
    
    
    # Initialize the class
    def __init__(self, browser):
        super().__init__(browser)
        self.browser.get('https://automationexercise.com/payment_done/900')
        self.wait_for_page_load()