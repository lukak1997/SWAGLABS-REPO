
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.components.footer_component import FooterComponent
from playwright.async_api import expect
from pages.components.header_component import HeaderComponent
from time import sleep
from pages.product_page import ProductPage





def footer_check(logged_in_page):
    footer_component = FooterComponent(logged_in_page)
    assert footer_component.get_twitter_link_href() == "https://twitter.com/saucelabs"
    assert footer_component.get_facebook_link_href() == "https://www.facebook.com/saucelabs"
    assert footer_component.get_linkedin_link_href() == "https://www.linkedin.com/company/sauce-labs/"
    assert footer_component.get_footer_text() == "© 2026 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy"

def test_products_logged_in_page_add_to_cart(logged_in_page):
    products_logged_in_page= ProductsPage(logged_in_page)
    assert products_logged_in_page.get_product_count() > 0
    header_component = HeaderComponent(logged_in_page)
    assert header_component.count_items_in_cart() == 0
    products_logged_in_page.click_add_to_cart_button("Sauce Labs Backpack")
    products_logged_in_page.click_add_to_cart_button("Test.allTheThings() T-Shirt (Red)")
    assert header_component.count_items_in_cart() == 2
    products_logged_in_page.click_add_to_cart_button("Sauce Labs Fleece Jacket")
    assert header_component.count_items_in_cart() == 3
    products_logged_in_page.click_remove_from_cart_button("Sauce Labs Fleece Jacket")
    assert header_component.count_items_in_cart() == 2
    footer_check(logged_in_page)


def test_products_logged_in_page_sorting(logged_in_page):
    products_logged_in_page= ProductsPage(logged_in_page)
    products_logged_in_page.select_sort_option("Price (low to high)")
    assert products_logged_in_page.get_product_count() > 0
    assert products_logged_in_page.get_prices() == sorted(products_logged_in_page.get_prices())
    products_logged_in_page.select_sort_option("Price (high to low)") 
    assert products_logged_in_page.get_product_count() > 0
    assert products_logged_in_page.get_prices() == sorted(products_logged_in_page.get_prices(), reverse=True) 
    products_logged_in_page.select_sort_option("Name (A to Z)")
    assert products_logged_in_page.get_product_count() > 0
    assert products_logged_in_page.get_names() == sorted(products_logged_in_page.get_names())
    products_logged_in_page.select_sort_option("Name (Z to A)")
    assert products_logged_in_page.get_product_count() > 0
    assert products_logged_in_page.get_names() == sorted(products_logged_in_page.get_names(), reverse=True)   
    
def test_product_logged_in_page(logged_in_page):
    products_logged_in_page= ProductsPage(logged_in_page)
    products_logged_in_page.click_product_img("Sauce Labs Onesie")
    header_component = HeaderComponent(logged_in_page)
    assert header_component.count_items_in_cart() == 0
    product_logged_in_page = ProductPage(logged_in_page)
    assert product_logged_in_page.get_product_title() == "Sauce Labs Onesie"
    assert product_logged_in_page.get_product_price() == "$7.99"   # MAKE THIS ASSERTION DYNAMIC
    footer_check(logged_in_page)
    



    


def test_cart_logged_in_page(logged_in_page):
    products_logged_in_page= ProductsPage(logged_in_page)
    assert products_logged_in_page.get_product_count() > 0
    header_component = HeaderComponent(logged_in_page)
    assert header_component.count_items_in_cart() == 0
    products_logged_in_page.click_add_to_cart_button("Sauce Labs Backpack")
    products_logged_in_page.click_add_to_cart_button("Test.allTheThings() T-Shirt (Red)")
    header_component.click_cart_icon()
    cart_logged_in_page = CartPage(logged_in_page)
    assert cart_logged_in_page.get_item_count() == 2
    assert cart_logged_in_page.is_item_in_cart("Sauce Labs Backpack")
    assert cart_logged_in_page.is_item_in_cart("Test.allTheThings() T-Shirt (Red)")
    assert header_component.count_items_in_cart() == 2

    cart_logged_in_page.remove_item("Sauce Labs Backpack")
    assert not cart_logged_in_page.is_item_in_cart("Sauce Labs Backpack")
    assert cart_logged_in_page.get_item_count() == 1
    assert header_component.count_items_in_cart() == 1


    cart_logged_in_page.remove_item("Test.allTheThings() T-Shirt (Red)")
    assert not cart_logged_in_page.is_item_in_cart("Test.allTheThings() T-Shirt (Red)")
    assert cart_logged_in_page.get_item_count() == 0
    assert header_component.count_items_in_cart() == 0
    cart_logged_in_page.click_continue_shopping()
    assert products_logged_in_page.get_product_count() > 0
    assert header_component.count_items_in_cart() == 0
    footer_check(logged_in_page)
   




