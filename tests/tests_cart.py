# import pytest
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from pytest_bdd import given, when, then, scenario
# from selenium.webdriver import ActionChains
# from selenium.webdriver.support.ui import Select

# # Test Fixture
# @pytest.fixture
# def browser():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     yield driver
#     driver.quit()

# # SCENARIO: Test the cart and invoice download
# @scenario('features/cart.feature', 'Create an account to complete an order and download the invoice')
# def test_cart():
#     pass

# @given('I add products to the cart')
# def add_products_to_cart(browser):
#     #Go to the website 
#     browser.get('https://automationexercise.com/')

#     #Handle cookies if any 
#     consentCookiesBtn = WebDriverWait(browser, 10).until(
#         EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]')),
#         message='Consent cookies button not found'
#     )
#     consentCookiesBtn.click()

#     WebDriverWait(browser, 10).until(
#         EC.presence_of_element_located((By.XPATH, '//*[@id="header"]/div/div')),
#         message='Automation website not found'
#     )
#     title = browser.find_element(By.XPATH, '//*[@id="slider-carousel"]/div/div[1]/div[1]/h1/span')
#     browser.execute_script("arguments[0].scrollIntoView();", title)
#     assert title.text == 'Automation', 'Title not found'

#     # #Hover on the first product and add it to the cart
#     product1 = browser.find_element(By.XPATH, '/html/body/section[2]/div/div/div[2]/div[1]')
#     browser.execute_script("arguments[0].scrollIntoView();", product1)

#     action = ActionChains(browser)
#     action.move_to_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/img").perform()

    # add2cart = browser.find_element(By.XPATH, "//div[@class='features_items']/div[2]//div[@class='product-overlay']//a[.='Add to cart']")    
    # add2cart.click()

    #Continue Shopping 

    #Click on the second product to add to the cart

    #Click on view cart 

    #Click on proceed to checkout

# @when('I create an account')
# def create_account(browser):
    #Click Register / Login 

    #Access login page

    #Fill form with name and email 

    #Click on Signup 

    #Reach the signup page 

    #Verify name and email are correct

    #Fill the form with password, name, first name, address, country, state, city, zip code, mobile 

    #Click on Create Account 

    #Verify the account is created

    #Click on continue 

# @when('I am logged in')
# def login(browser):
    #Verify the user is logged in (logged in as name)

    #Verify the logout button is displayed

    #Delete Account button is displayed

# @then('I can finalize the purchase')
# def checkout(browser):
    #Click to the cart 

    #Verify products are in the cart

    #Click on proceed to checkout

    #Verify the address is correct

    #Click on place order 

    #Reach payment page 

    #Fill the form with card number, expiration date, CVV

    #Click on Pay and confirm order