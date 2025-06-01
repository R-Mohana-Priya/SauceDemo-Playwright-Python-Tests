# tests/test_logout.py

def test_logout(page):
    page.click("#react-burger-menu-btn")
    page.locator("#logout_sidebar_link").click()
    assert page.url == "https://www.saucedemo.com/"
