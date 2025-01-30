# tests/test_add_product.py
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytest_bdd import given, when, then, scenario
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.home_page import HomePage
from pages.cart_page import CartPage

# Test Fixture
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_add_product_to_cart(browser):
    home_page = HomePage(browser)
    home_page.accept_cookies()
    # home_page.add_product_to_cart()

    # cart_page = CartPage(browser)
    # cart_page.go_to_cart()
    # cart_page.proceed_to_checkout()
