from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class ProductsPage(BasePage):

    # Locators
    SEARCH_PRODUCTS_FIELD = (By.XPATH, "//input[@id='search_product']")
    SEARCH_PRODUCTS_BTN = (By.XPATH, "//button[@id='submit_search']")
    PRODUCTS_LIST = (By.XPATH, "/html/body/section[2]/div/div/div[2]/div")
    PRODUCT1_CARD = (By.XPATH, "/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]")
    PRODUCT1_ADD_TO_CART_BTN = (By.XPATH, "//div[@class='features_items']/div[2]//div[@class='product-overlay']//a[.='Add to cart']")
    PRODUCT2_CARD = (By.XPATH, "/html/body/section[2]/div/div/div[2]/div/div[3]")
    PRODUCT2_ADD_TO_CART_BTN = (By.XPATH, "//div[@class='features_items']/div[3]//div[@class='product-overlay']//a[.='Add to cart']")
    VIEW_PRODUCT1_DETAILS_BTN = (By.XPATH, "//a[@href='/product_details/3']")
    VIEW_PRODUCT2_DETAILS_BTN = (By.XPATH, "//a[@href='/product_details/4']")
    VIEW_CART_BTN = (By.XPATH, "//u[.='View Cart']")
    CONTINUE_SHOPPING_BTN = (By.XPATH, "//button[@class='btn btn-success close-modal btn-block']")
    
    # Initialize the class
    def __init__(self, browser):
        super().__init__(browser)
        self.browser.get('https://automationexercise.com/products')
        self.wait_for_page_load()

    