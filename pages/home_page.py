# pages/home_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):
    CONSENT_COOKIES_BTN = (By.XPATH, '/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]')
    PRODUCT1_ADD_TO_CART_BTN = (By.XPATH, "//a[contains(@href, 'add_to_cart=1')]")

    def __init__(self, browser):
        super().__init__(browser)
        self.browser.get('https://automationexercise.com/')
        self.wait_for_page_load()

    def accept_cookies(self):
        try:
            cookie_button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]'))
            )
            cookie_button.click()
        except:
            print("No cookies consent button found, proceeding.")

    def add_product_to_cart(self):
        self.click_element(self.PRODUCT1_ADD_TO_CART_BTN)
