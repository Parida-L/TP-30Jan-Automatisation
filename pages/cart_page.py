# pages/cart_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    VIEW_CART_BTN = (By.XPATH, "//a[contains(text(),'Cart')]")
    CHECKOUT_BTN = (By.XPATH, "//a[contains(text(),'Proceed To Checkout')]")

    # Click on the view cart button
    def go_to_cart(self):
        self.click_element(self.VIEW_CART_BTN)
    # Click on the proceed to checkout button
    def proceed_to_checkout(self):
        self.click_element(self.CHECKOUT_BTN)
