# tests/test_login.py

import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        yield page
        browser.close()

def test_login_success(page):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    assert page.url == "https://www.saucedemo.com/inventory.html"
    assert page.locator(".inventory_list").is_visible()

def test_login_failure(page):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "wrong_user")
    page.fill("#password", "wrong_pass")
    page.click("#login-button")
    assert page.locator("[data-test='error']").is_visible()
