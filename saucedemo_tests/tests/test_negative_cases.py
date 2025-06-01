# tests/test_negative_cases.py

def test_login_empty_fields(page):
    page.goto("https://www.saucedemo.com/")
    page.click("#login-button")
    assert page.locator("[data-test='error']").is_visible()

def test_login_only_username(page):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.click("#login-button")
    assert page.locator("[data-test='error']").is_visible()

def test_login_only_password(page):
    page.goto("https://www.saucedemo.com/")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    assert page.locator("[data-test='error']").is_visible()
