from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time

class AccountCreatedPage(BasePage):

    # Locators
    TITLE = (By.XPATH, "//*[@id='form']/div/div/div/h2")
    CONFIRMATION_TEXT = (By.XPATH, "//*[@id='form']/div/div/div/p[1]")
    CONTINUE_BTN = (By.XPATH, "//*[@id='form']/div/div/div/div/a")
    
    # Initialize the class
    def __init__(self, browser):
        super().__init__(browser)
        self.browser.get('https://automationexercise.com/account_created')
        self.wait_for_page_load()

    # Get the title of the page
    def get_title(self):
        return self.get_text(self.TITLE)
    
    # Get the confirmation text
    def get_confirmation_text(self):
        return self.get_text(self.CONFIRMATION_TEXT)
    
    # Click the Continue button (after verifying the btn is clickable)
    def click_continue_btn(self):
        self.click_element(self.CONTINUE_BTN)

    