import os
from dotenv import load_dotenv
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from playwright.async_api import expect
from pages.components.header_component import HeaderComponent
from time import sleep

from tests.pages import product_page


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
    header_component = HeaderComponent(page)
    assert header_component.count_items_in_cart() == 0
    products_page.click_add_to_cart_button("Sauce Labs Backpack")
    products_page.click_add_to_cart_button("Test.allTheThings() T-Shirt (Red)")
    assert header_component.count_items_in_cart() == 2
    products_page.click_add_to_cart_button("Sauce Labs Fleece Jacket")
    assert header_component.count_items_in_cart() == 3
    products_page.click_remove_from_cart_button("Sauce Labs Fleece Jacket")
    assert header_component.count_items_in_cart() == 2 


def test_cart_page(page):
    log_in(page)
    products_page= ProductsPage(page)
    assert products_page.get_product_count() > 0
    header_component = HeaderComponent(page)
    assert header_component.count_items_in_cart() == 0
    products_page.click_add_to_cart_button("Sauce Labs Backpack")
    products_page.click_add_to_cart_button("Test.allTheThings() T-Shirt (Red)")
    header_component.click_cart_icon()
    cart_page = CartPage(page)
    assert cart_page.get_item_count() == 2
    assert cart_page.is_item_in_cart("Sauce Labs Backpack")
    assert cart_page.is_item_in_cart("Test.allTheThings() T-Shirt (Red)")
    assert header_component.count_items_in_cart() == 2

    cart_page.remove_item("Sauce Labs Backpack")
    assert not cart_page.is_item_in_cart("Sauce Labs Backpack")
    assert cart_page.get_item_count() == 1
    assert header_component.count_items_in_cart() == 1


    cart_page.remove_item("Test.allTheThings() T-Shirt (Red)")
    assert not cart_page.is_item_in_cart("Test.allTheThings() T-Shirt (Red)")
    assert cart_page.get_item_count() == 0
    assert header_component.count_items_in_cart() == 0
    cart_page.click_continue_shopping()
    assert products_page.get_product_count() > 0
    assert header_component.count_items_in_cart() == 0
   




