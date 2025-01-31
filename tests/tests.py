# tests/test_add_product.py
import pytest
import time
from selenium import webdriver
from pytest_bdd import scenarios, given, when, then

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.home_page import HomePage
from pages.view_cart_page import ViewCartPage
from pages.login_page import LoginPage
from fixtures.random_email_generator import generate_random_email
from pages.signup_page import SignupPage
from fixtures.password_generator import generate_secure_password
from pages.account_created import AccountCreatedPage

# Load feature file
scenarios("features/cart.feature")

# Test Fixture for browser setup
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@given("I add products to the cart")
def add_products_to_cart(browser):
    home_page = HomePage(browser)
    home_page.accept_cookies()
    # Add one product to cart
    home_page.add_product1_to_cart()
    # Click on continue shopping
    home_page.continue_shopping_modal()
    # Add second product to cart
    home_page.add_product2_to_cart()
    # Click on view cart
    home_page.view_cart_modal()
    # Verify products are in the cart
    view_cart_page = ViewCartPage(browser)
    assert view_cart_page.is_products_list_present()
    # Proceed to checkout
    view_cart_page.proceed_to_checkout()
    assert view_cart_page.is_modal_present()
    # Click on register/login on the modal
    view_cart_page.register_login_modal()


@when("I create an account")
def create_account(browser):
    #Login Page
    login_page = LoginPage(browser)
    # Generate random email
    random_email = generate_random_email()
    # Signup with random email
    login_page.signup(name="Test User", email=random_email)

    #Signup Page
    # Fill in the signup form
    signup_page = SignupPage(browser)
    signup_page.click_mr_radio_btn()
    assert signup_page.get_name_value() == "Test User"
    assert signup_page.get_email_value() == random_email
    random_password = generate_secure_password()
    signup_page.fill_password(random_password)
    signup_page.fill_first_name("Test")
    signup_page.fill_last_name("User")
    signup_page.fill_address("123 Test Street")
    signup_page.select_country()
    signup_page.fill_state("Test State")
    signup_page.fill_zip_code("123456")
    signup_page.fill_phone("1234567890")
    # Click Create Account
    signup_page.click_create_account_btn()

    #Account Created Page 
    account_created_page = AccountCreatedPage(browser)
    assert account_created_page.get_title() == "ACCOUNT CREATED!"
    confirmation_text = account_created_page.get_confirmation_text()
    assert "account has been successfully created!" in confirmation_text
    # Click Continue after the account is created
    account_created_page.click_continue_btn()

#TODO : TERMINER LE TP