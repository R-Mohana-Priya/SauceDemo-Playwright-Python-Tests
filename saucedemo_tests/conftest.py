# conftest.py

import os
import pytest
from datetime import datetime
from playwright.sync_api import sync_playwright

os.makedirs("screenshots", exist_ok=True)

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        yield page
        browser.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    import pytest_html
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call":
        page = item.funcargs.get("page", None)
        if page:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"screenshots/{item.name}_{timestamp}.png"
            page.screenshot(path=filename, full_page=True)
            if hasattr(rep, "extra"):
                rep.extra.append(pytest_html.extras.image(filename))
            else:
                rep.extra = [pytest_html.extras.image(filename)]
