# pages/home_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time
class HomePage(BasePage):

    # Locators
    CONSENT_COOKIES_BTN = (By.XPATH, '/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]')
    PRODUCT1_CARD = (By.XPATH, "/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[1]")
    PRODUCT1_ADD_TO_CART_BTN = (By.XPATH, "/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/div[2]/div/a")
    PRODUCT1_VIEW_DETAILS_BTN = (By.XPATH, "//a[@href='/product_details/1']")
    PRODUCT2_CARD = (By.XPATH, "/html/body/section[2]/div/div/div[2]/div[1]/div[3]/div/div[1]/div[1]/p")
    PRODUCT2_ADD_TO_CART_BTN = (By.XPATH, "//div[@class='features_items']/div[3]//div[@class='product-overlay']//a[.='Add to cart']")
    PRODUCT2_VIEW_DETAILS_BTN = (By.XPATH, "//a[@href='/product_details/2']")
    HOME_NAV_BTN = (By.XPATH, "//a[contains(.,'Home')]")
    PRODUCTS_NAV_BTN = (By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[3]/a")
    CART_NAV_BTN = (By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[3]/a")
    LOGIN_NAV_BTN = (By.XPATH, "//a[contains(.,'Signup / Login')]")
    CONTINUE_SHOPPING_BTN = (By.XPATH, "//button[@class='btn btn-success close-modal btn-block']")
    VIEW_CART_BTN = (By.XPATH, "//u[.='View Cart']")
    MODAL_CART = (By.XPATH, "//*[@id='cartModal']/div/div")

    #AS LOGGED IN USER
    LOGOUT_NAV_BTN = (By.XPATH, "//a[contains(.,'Logout')]") 
    DELETE_ACCOUNT_BTN = (By.XPATH, "//a[contains(.,'Delete Account')]")
    LOGGED_IN_MSG = (By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[10]/a/text()") # Logged in as USERNAME
    CART_BTN = (By.XPATH, "//ul[@class='nav navbar-nav']//a[contains(.,'Cart')]")

    # Initialize the class
    def __init__(self, browser):
        super().__init__(browser)
        self.browser.get('https://automationexercise.com/')
        self.wait_for_page_load()

    # Accept cookies
    def accept_cookies(self):
        try:
            self.click_element(self.CONSENT_COOKIES_BTN)
        except:
            print("No cookies consent button found, proceeding.")

    # Add product to cart
    def add_product1_to_cart(self):
        self.find_product1()
        self.scroll_to_element(self.PRODUCT1_CARD)
        time.sleep(1)
        self.hover_over_element(self.PRODUCT1_CARD)
        time.sleep(1)
        self.is_element_visible(self.PRODUCT1_ADD_TO_CART_BTN)
        # self.scroll_to_element(self.PRODUCT1_ADD_TO_CART_BTN)
        self.click_element(self.PRODUCT1_ADD_TO_CART_BTN)
        time.sleep(1)

    def find_product1(self):
        self.is_element_visible(self.PRODUCT1_CARD)
        actual_text = self.get_text(self.PRODUCT1_CARD).strip()
        assert "Blue Top" in actual_text, f"Product name not found! Extracted: '{actual_text}'"
    
    def add_product2_to_cart(self):
        self.find_product2()
        self.scroll_to_element(self.PRODUCT2_CARD)
        time.sleep(1)
        self.hover_over_element(self.PRODUCT2_ADD_TO_CART_BTN)
        time.sleep(1)
        self.click_element(self.PRODUCT2_ADD_TO_CART_BTN)
        time.sleep(1)

    def find_product2(self):
        self.is_element_visible(self.PRODUCT2_CARD)
        actual_text = self.get_text(self.PRODUCT2_CARD).strip()
        assert "Men Tshirt" in actual_text, f"Product name not found! Extracted: '{actual_text}'"

    def is_modal_present(self):
        return self.is_element_visible(self.MODAL_CART)

    def continue_shopping_modal(self):
        self.is_modal_present()
        self.click_element(self.CONTINUE_SHOPPING_BTN)

    def view_cart_modal(self):
        self.is_modal_present()
        self.click_element(self.VIEW_CART_BTN)

    def view_product1_details(self):
        self.click_element(self.PRODUCT1_VIEW_DETAILS_BTN)

    def view_product2_details(self):
        self.click_element(self.PRODUCT2_VIEW_DETAILS_BTN)

    # Navigation
    def go_to_home(self):
        self.click_element(self.HOME_NAV_BTN)
    def go_to_products(self):
        self.click_element(self.PRODUCTS_NAV_BTN)
    def go_to_login(self):
        self.click_element(self.LOGIN_NAV_BTN)
        
    def go_to_cart(self):
        self.click_element(self.CART_NAV_BTN)

    # AS LOGGED IN USER
    def click_logout(self):
        self.click_element(self.LOGOUT_NAV_BTN)
    
    def click_delete_account(self):
        self.click_element(self.DELETE_ACCOUNT_BTN)

    def is_logged_in(self):
        self.is_element_visible(self.LOGOUT_NAV_BTN)
        self.is_element_visible(self.DELETE_ACCOUNT_BTN)
        return self.is_element_visible(self.LOGGED_IN_MSG)

    def logged_in_as(self):
        return self.get_text(self.LOGGED_IN_MSG)
