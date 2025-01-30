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
    CITY_INPUT_FIELD = (By.XPATH, "//input[@id='city']")
    STATE_INPUT_FIELD = (By.XPATH, "//input[@id='state']")
    ZIP_CODE_INPUT_FIELD = (By.XPATH, "//input[@id='zipcode']")
    PHONE_INPUT_FIELD = (By.XPATH, "//input[@id='mobile_number']")
    CREATE_ACCOUNT_BTN = (By.XPATH, "//button[.='Create Account']")

    # Initialize the class
    def __init__(self, browser):
        super().__init__(browser)
        self.browser.get('https://automationexercise.com/signup')
        self.wait_for_page_load()

    # Click the Mr radio button
    def click_mr_radio_btn(self):
        self.click_element(self.MR_RADIO_BTN)

    # Fill the email field
    def fill_email(self, random_email):
        self.enter_text(self.EMAIL_INPUT_FIELD, email)