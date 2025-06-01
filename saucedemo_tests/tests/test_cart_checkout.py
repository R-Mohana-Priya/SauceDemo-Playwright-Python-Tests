# tests/test_cart_checkout.py

def test_add_to_cart_and_validate_total(page):
    # Add first two products to cart
    add_buttons = page.locator("button.btn_inventory")
    add_buttons.nth(0).click()
    add_buttons.nth(1).click()
    page.click(".shopping_cart_link")

    # Verify cart has 2 items
    cart_items = page.locator(".cart_item")
    assert cart_items.count() == 2

    # Get prices and sum them
    prices_text = cart_items.locator(".inventory_item_price").all_inner_texts()
    prices = [float(p.replace("$", "")) for p in prices_text]
    expected_total = sum(prices)

    # Proceed to checkout info page
    page.click("#checkout")
    page.fill("#first-name", "Test")
    page.fill("#last-name", "User")
    page.fill("#postal-code", "12345")
    page.click("#continue")

    # Verify item total on overview page matches sum
    item_total_text = page.locator(".summary_subtotal_label").inner_text()
    item_total = float(item_total_text.split("$")[1])
    assert abs(item_total - expected_total) < 0.01


def test_checkout_complete(page):
    # Add one product to cart and checkout fully
    page.locator("button.btn_inventory").first.click()
    page.click(".shopping_cart_link")
    page.click("#checkout")
    page.fill("#first-name", "Test")
    page.fill("#last-name", "User")
    page.fill("#postal-code", "12345")
    page.click("#continue")
    page.click("#finish")

    # Verify success message
    assert page.inner_text(".complete-header") == "Thank you for your order!"
