from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class BasePage:
    # Base class for all pages
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 15)

    # Wait for the page to load
    def wait_for_page_load(self):
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    # Click on an element
    def click_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
    # Enter text into a text field
    def enter_text(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)
    # Get the text of an element
    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text
    # Scroll to an element
    def scroll_to_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.browser.execute_script("arguments[0].scrollIntoView();", element)
    # Hover over an element
    def hover_over_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        ActionChains(self.browser).move_to_element(element).perform()