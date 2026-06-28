import os
from dotenv import load_dotenv
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from playwright.async_api import expect


load_dotenv(dotenv_path=".env", override=True)

def log_in(page):
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    page.goto("https://www.saucedemo.com/")
    print("!!!!!!!!!")
    print(username)
    print(password)
    login_page = LoginPage(page)
    login_page.write_username(username) 
    login_page.write_password(password) 
    login_page.click_login()

def test_products_page(page):
    log_in(page)
    products_page= ProductsPage(page)
    assert products_page.get_product_count() > 0
    products_page.click_add_to_cart_button("Sauce Labs Backpack")
    products_page.click_add_to_cart_button("Test.allTheThings() T-Shirt (Red)")

