# tests/test_sorting.py

def test_sort_price_low_to_high(page):
    page.goto("https://www.saucedemo.com/inventory.html")
    page.select_option(".product_sort_container", "lohi")
    prices = page.locator(".inventory_item_price").all_inner_texts()
    prices_float = [float(p.replace("$", "")) for p in prices]
    assert prices_float == sorted(prices_float)

def test_sort_price_high_to_low(page):
    page.goto("https://www.saucedemo.com/inventory.html")
    page.select_option(".product_sort_container", "hilo")
    prices = page.locator(".inventory_item_price").all_inner_texts()
    prices_float = [float(p.replace("$", "")) for p in prices]
    assert prices_float == sorted(prices_float, reverse=True)
