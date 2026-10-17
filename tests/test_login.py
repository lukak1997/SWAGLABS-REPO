import re

from pages.login_page import LoginPage
from playwright.sync_api import expect


LOGIN_URL = "https://www.saucedemo.com/"


def test_login_page_displays_controls_and_accepted_credentials(page):
    page.goto(LOGIN_URL)
    login_page = LoginPage(page)

    expect(page).to_have_title("Swag Labs")
    expect(login_page.username_field).to_be_visible()
    expect(login_page.password_field).to_be_visible()
    expect(login_page.login_button).to_be_visible()
    credentials = page.locator(".login_credentials")
    for username in [
        "standard_user",
        "locked_out_user",
        "problem_user",
        "performance_glitch_user",
        "error_user",
        "visual_user",
    ]:
        expect(credentials).to_contain_text(username)
    expect(page.locator(".login_password")).to_contain_text("secret_sauce")


def test_login_requires_username_when_form_is_empty(page):
    page.goto(LOGIN_URL)
    login_page = LoginPage(page)
    expect(login_page.username_field).to_be_visible()
    expect(login_page.password_field).to_be_visible()
    expect(login_page.login_button).to_be_visible()

    login_page.click_login()
    expect(page.locator('[data-test="error"]')).to_contain_text(
        "Epic sadface: Username is required"
    )


def test_standard_user_rejects_incorrect_password(page):
    page.goto(LOGIN_URL)
    login_page = LoginPage(page)
    expect(login_page.username_field).to_be_visible()
    expect(login_page.password_field).to_be_visible()
    expect(login_page.login_button).to_be_visible()

    login_page.write_username("standard_user")
    login_page.write_password("wrong_password")
    login_page.click_login()
    expect(page.locator('[data-test="error"]')).to_contain_text(
        "Epic sadface: Username and password do not match any user in this service"
    )


def test_locked_out_user_sees_locked_out_message(page):
    page.goto(LOGIN_URL)
    login_page = LoginPage(page)
    expect(login_page.username_field).to_be_visible()
    expect(login_page.password_field).to_be_visible()
    expect(login_page.login_button).to_be_visible()

    login_page.write_username("locked_out_user")
    login_page.write_password("secret_sauce")
    login_page.click_login()
    expect(page.locator('[data-test="error"]')).to_contain_text(
        "Epic sadface: Sorry, this user has been locked out."
    )


def test_standard_user_logs_in_successfully(page):
    page.goto(LOGIN_URL)
    login_page = LoginPage(page)
    expect(login_page.username_field).to_be_visible()
    expect(login_page.password_field).to_be_visible()
    expect(login_page.login_button).to_be_visible()

    login_page.write_username("standard_user")
    login_page.write_password("secret_sauce")
    login_page.click_login()
    expect(page).to_have_url(re.compile(r".*/inventory\.html$"))
