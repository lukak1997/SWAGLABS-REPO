import os
from dotenv import load_dotenv

load_dotenv()

def test_log_in(page):
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    page.goto("https://www.saucedemo.com/")
    username_field = page.locator('[data-test="username"]')
    password_field = page.locator('[data-test="password"]')
    login_button = page.locator('[data-test="login-button"]')
    username_field.fill(username)
    password_field.fill(password)
    login_button.click() 


