import pytest
from playwright.sync_api import sync_playwright
import os
from dotenv import load_dotenv
from tests.pages.login_page import LoginPage

load_dotenv(dotenv_path=".env", override=True)

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()


@pytest.fixture
def logged_in_page(page):
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
    return page        