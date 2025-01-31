from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class SignupPage(BasePage):

    # Locators
    MR_RADIO_BTN = (By.XPATH, "//input[@value='Mr']")
    MRS_RADIO_BTN = (By.XPATH, "//input[@value='Mrs']")
    NAME_INPUT_FIELD = (By.XPATH, "//input[@id='name']") #already filled with previous name (login page)
    EMAIL_INPUT_FIELD = (By.XPATH, "//input[@id='email']") #already filled with previous email (login page) NOT CLICKABLE
    PASSWORD_INPUT_FIELD = (By.XPATH, "//input[@id='password']")
    FIRST_NAME_INPUT_FIELD = (By.XPATH, "//input[@id='first_name']")
    LAST_NAME_INPUT_FIELD = (By.XPATH, "//input[@id='last_name']")
    ADDRESS_INPUT_FIELD = (By.XPATH, "//p[4]/input[@class='form-control']")
    COUNTRY_SELECT_FIELD = (By.XPATH, "//select[@id='country']")
    COUNTRY_SELECTION = (By.XPATH, "//*[@id='country']/option[7]")
    CITY_INPUT_FIELD = (By.XPATH, "//input[@id='city']")
    STATE_INPUT_FIELD = (By.XPATH, "//input[@id='state']")
    ZIP_CODE_INPUT_FIELD = (By.XPATH, "//input[@id='zipcode']")
    PHONE_INPUT_FIELD = (By.XPATH, "//input[@id='mobile_number']")
    CREATE_ACCOUNT_BTN = (By.XPATH, "//button[.='Create Account']")

    # Initialize the class
    def __init__(self, browser):
        super().__init__(browser)
        #self.browser.get('https://automationexercise.com/signup')
        self.wait_for_page_load()

    # Click the Mr radio button
    def click_mr_radio_btn(self):
        self.click_element(self.MR_RADIO_BTN)

    def click_mrs_radio_btn(self):
        self.click_element(self.MRS_RADIO_BTN)

    # Fill Password - Mandatory Field
    def fill_password(self, password):
        self.enter_text(self.PASSWORD_INPUT_FIELD, password)

    # Fill First Name - Mandatory Field
    def fill_first_name(self, first_name):
        self.scroll_to_element(self.FIRST_NAME_INPUT_FIELD)
        self.enter_text(self.FIRST_NAME_INPUT_FIELD, first_name)

    # Fill Last Name - Mandatory Field
    def fill_last_name(self, last_name):
        self.enter_text(self.LAST_NAME_INPUT_FIELD, last_name)

    # Fill Address - Mandatory Field
    def fill_address(self, address):
        self.scroll_to_element(self.ADDRESS_INPUT_FIELD)
        self.enter_text(self.ADDRESS_INPUT_FIELD, address)

    # Select Country - Mandatory Field
    def select_country(self):
        self.scroll_to_element(self.COUNTRY_SELECT_FIELD)
        self.click_element(self.COUNTRY_SELECT_FIELD)
        self.click_element(self.COUNTRY_SELECTION)

    # Fill State - Mandatory Field
    def fill_state(self, state):
        self.enter_text(self.STATE_INPUT_FIELD, state)

    # Fill City - Mandatory Field
    def fill_city(self, city):
        self.scroll_to_element(self.CITY_INPUT_FIELD)
        self.enter_text(self.CITY_INPUT_FIELD, city)

    # Fill Zip Code - Mandatory Field
    def fill_zip_code(self, zip_code):
        self.enter_text(self.ZIP_CODE_INPUT_FIELD, zip_code)

    # Fill Phone - Mandatory Field
    def fill_phone(self, phone):
        self.scroll_to_element(self.PHONE_INPUT_FIELD)
        self.enter_text(self.PHONE_INPUT_FIELD, phone)

    # Check if the Create Account button is clickable
    def is_create_account_btn_clickable(self):
        return self.is_element_clickable(self.CREATE_ACCOUNT_BTN)

    # Click Create Account Button
    def click_create_account_btn(self):
        self.scroll_to_element(self.CREATE_ACCOUNT_BTN)
        self.click_element(self.CREATE_ACCOUNT_BTN)    

    def get_name_value(self):
        return self.get_value(self.NAME_INPUT_FIELD)
    
    def get_email_value(self):
         return self.get_value(self.EMAIL_INPUT_FIELD)