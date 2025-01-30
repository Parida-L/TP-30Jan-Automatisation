# pages/home_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
class HomePage(BasePage):

    # Locators
    CONSENT_COOKIES_BTN = (By.XPATH, '/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]')
    PRODUCT1_CARD = (By.XPATH, "//div[@class='features_items']/div[2]//div[@class='product-overlay']")
    PRODUCT1_ADD_TO_CART_BTN = (By.XPATH, "//div[@class='features_items']/div[2]//div[@class='product-overlay']//a[.='Add to cart']")
    PRODUCT1_VIEW_DETAILS_BTN = (By.XPATH, "//a[@href='/product_details/1']")
    PRODUCT2_CARD = (By.XPATH, "//div[@class='features_items']/div[3]//div[@class='product-overlay']")
    PRODUCT2_ADD_TO_CART_BTN = (By.XPATH, "//div[@class='features_items']/div[3]//div[@class='product-overlay']//a[.='Add to cart']")
    PRODUCT2_VIEW_DETAILS_BTN = (By.XPATH, "//a[@href='/product_details/2']")
    HOME_NAV_BTN = (By.XPATH, "//a[contains(.,'Home')]")
    PRODUCTS_NAV_BTN = (By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[3]/a")
    CART_NAV_BTN = (By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[3]/a")
    LOGIN_NAV_BTN = (By.XPATH, "//a[contains(.,'Signup / Login')]")
    CONTINUE_SHOPPING_BTN = (By.XPATH, "//button[@class='btn btn-success close-modal btn-block']")
    VIEW_CART_BTN = (By.XPATH, "//u[.='View Cart']")

    # Initialize the class
    def __init__(self, browser):
        super().__init__(browser)
        self.browser.get('https://automationexercise.com/')
        self.wait_for_page_load()

    # Accept cookies
    def accept_cookies(self):
        try:
            self.click_element(self.CONSENT_COOKIES_BTN)
            # cookie_button = self.wait.until(
            # EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]'))
            # )
            # cookie_button.click()
        except:
            print("No cookies consent button found, proceeding.")

    # Add product to cart
    def add_product1_to_cart(self):
        # Hover over the product
        self.hover_over_element(self.PRODUCT1_ADD_TO_CART_BTN)
        self.click_element(self.PRODUCT1_ADD_TO_CART_BTN)

    def add_product2_to_cart(self):
        # Hover over the product
        self.hover_over_element(self.PRODUCT2_ADD_TO_CART_BTN)
        self.click_element(self.PRODUCT2_ADD_TO_CART_BTN)

    def view_product1_details(self):
        self.click_element(self.PRODUCT1_VIEW_DETAILS_BTN)

    def view_product2_details(self):
        self.click_element(self.PRODUCT2_VIEW_DETAILS_BTN)

    def go_to_home(self):
        self.click_element(self.HOME_NAV_BTN)

    def go_to_products(self):
        self.click_element(self.PRODUCTS_NAV_BTN)

    def go_to_login(self):
        self.click_element(self.LOGIN_NAV_BTN)

    def go_to_cart(self):
        self.click_element(self.CART_NAV_BTN)