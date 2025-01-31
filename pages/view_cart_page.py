# pages/cart_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class ViewCartPage(BasePage):
    VIEW_CART_NAV_BTN = (By.XPATH, "//a[contains(text(),'Cart')]")
    CHECKOUT_BTN = (By.XPATH, "//a[contains(text(),'Proceed To Checkout')]")
    REGISTER_LOGIN_BTN = (By.XPATH, "//u[.='Register / Login']")
    CONTINUE_CART_BTN = (By.XPATH, "//button[@class='btn btn-success close-checkout-modal btn-block']")
    CHECKOUT_MODAL = (By.XPATH, "//*[@id='checkoutModal']/div/div")
    PRODUCTS_CART_TABLE_LIST = (By.XPATH, "//*[@id='cart_info']")

    # Initialize the class
    def __init__(self, browser):
        super().__init__(browser)
        self.browser.get('https://automationexercise.com/view_cart')
        self.wait_for_page_load()

    # Click on the proceed to checkout button
    def proceed_to_checkout(self):
        self.click_element(self.CHECKOUT_BTN)
        time.sleep(2)

    def is_products_list_present(self):
        return self.is_element_visible(self.PRODUCTS_CART_TABLE_LIST)

    def is_modal_present(self):
        return self.is_element_visible(self.CHECKOUT_MODAL)
    
    def continue_on_cart_modal(self):
        self.click_element(self.CONTINUE_CART_BTN)

    def register_login_modal(self):
        self.click_element(self.REGISTER_LOGIN_BTN)

    