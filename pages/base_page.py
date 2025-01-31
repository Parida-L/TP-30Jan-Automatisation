from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class BasePage:
    # Base class for all pages
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 15)

    # Wait for the page to load
    def wait_for_page_load(self):
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Click on an element after verifying it is clickable
    def click_element(self, locator):
        # try:
        #     self.wait.until(EC.presence_of_element_located(locator))  
        #     element = self.wait.until(EC.visibility_of_element_located(locator))  
        #     element.click()
        # except:
        #     self.browser.save_screenshot("error_click.png")  
        #     self.browser.execute_script("arguments[0].click();", element) 
        try:
            self.wait.until(EC.presence_of_element_located(locator))  
            element = self.wait.until(EC.visibility_of_element_located(locator))  
            element.click()
        except Exception as e:
            print(f"⚠️ Click failed on {locator}, saving screenshot: error_click.png")
            self.browser.save_screenshot("error_click.png")

            # Ensure element is defined before JavaScript click
            try:
                element = self.browser.find_element(*locator)
                self.browser.execute_script("arguments[0].click();", element)
                print("JavaScript click successful")
            except Exception as js_error:
                print(f"JavaScript click also failed: {js_error}")
                raise e  # Re-raise original exception if all fails

    # Enter text into a text field  after verifying it is visible
    def enter_text(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)
    # Get the text of an element after verifying it is visible
    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text
    
    #Get the value of an element after verifying it is visible
    def get_value(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).get_attribute("value")
    
    # Scroll to an element after verifying it is visible
    def scroll_to_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.browser.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)

    # Hover over an element after verifying it is visible
    def hover_over_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        time.sleep(1)
        ActionChains(self.browser).move_to_element(element).perform()

    # Check if an element is clickable 
    def is_element_clickable(self, locator):
        try:
            self.wait.until(EC.element_to_be_clickable(locator))
            return True
        except:
            return False
        
    # Check if an element is visible
    def is_element_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False
        
    # Check if input field is editable
    def is_field_editable(self, field_locator):
        """        
        :param field_locator: Tuple containing locator strategy and value (e.g., (By.ID, "email"))
        :return: True if the field is enabled and not readonly, False otherwise
        """
        # Find the web element using the provided locator
        element = self.browser.find_element(*field_locator)
        # Check if the element is enabled (i.e., not disabled)
        is_enabled = element.is_enabled()
        # Check if the element has the 'readonly' attribute (returns None if the attribute is not set)
        is_not_readonly = element.get_attribute("readonly") is None
        # Return True if the field is both enabled and not readonly, otherwise return False
        return is_enabled and is_not_readonly