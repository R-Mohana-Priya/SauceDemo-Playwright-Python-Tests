# tests/test_display_products.py

def test_products_displayed(page):
    items = page.locator(".inventory_item")
    assert items.count() > 0

    for i in range(items.count()):
        assert items.nth(i).locator(".inventory_item_name").is_visible()
        assert items.nth(i).locator(".inventory_item_price").is_visible()
