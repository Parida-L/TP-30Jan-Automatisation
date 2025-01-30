from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class LoginPage(BasePage):

    # Locators
    LOGIN_EMAIL_FIELD = (By.XPATH, "//div[@class='login-form']//input[@name='email']")
    LOGIN_PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
    LOGIN_BTN = (By.XPATH, "//button[.='Login']")
    NAME_REGISTER_FIELD = (By.XPATH, "//input[@name='name']")
    EMAIL_REGISTER_FIELD = (By.XPATH, "//div[@class='signup-form']//input[@name='email']")
    SIGNUP_BTN = (By.XPATH, "//button[.='Signup']")
    
    # Initialize the class
    def __init__(self, browser):
        super().__init__(browser)
        self.browser.get('https://automationexercise.com/login')
        self.wait_for_page_load()

    # Enter email in the email field
    def enter_email(self, email):
        self.enter_text(self.LOGIN_EMAIL_FIELD, email)

    # Enter password in the password field
    def enter_password(self, password):
        self.enter_text(self.LOGIN_PASSWORD_FIELD, password)

    # Click the login button
    def click_login_btn(self):
        self.click_element(self.LOGIN_BTN)

    # Perform login action
    def login(self, email, password):
        """Enter credentials and click login"""
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_btn()

    # Enter name in the name field
    def enter_new_name(self, name):
        self.enter_text(self.NAME_REGISTER_FIELD, name)

    # Enter email in the email field
    def enter_new_email(self, email):
        self.enter_text(self.EMAIL_REGISTER_FIELD, email)

    # Click the signup button
    def click_signup_btn(self):
        self.click_element(self.SIGNUP_BTN)