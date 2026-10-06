from playwright.sync_api import expect
from Pages.LoginPage import LoginPage
from Pages.CheckoutPage import CheckoutPage
from Pages.OrderConfirmationPage import OrderConfirmationPage
from Pages.ProductPage import ProductPage
from Pages.CartPage import CartPage
from decimal import Decimal, ROUND_HALF_UP
import pytest
import json
from config import BASE_URL

with open("Data/test_data.json") as f:
    test_data = json.load(f)

 
invalid_credentials_list = []
for credential in test_data["invalid_credentials"]:
    invalid_credentials_list.append((credential["username"],credential["password"], credential["error"]))


checkout_validation_list = []
for cred in test_data["checkout_validation"]:
    checkout_validation_list.append((cred["first_name"], cred["last_name"], cred["zip"], cred["error"]))


@pytest.mark.parametrize("username, password, error", invalid_credentials_list)
def test_invalid_login(page, username, password, error):
    login_obj = LoginPage(page)
    login_obj.goto_website()
    login_obj.login(username, password)
    expect(page.locator("[data-test='error']")).to_have_text(error)
    expect(login_obj.login_btn).to_be_visible()
    expect(page).to_have_url(f"{BASE_URL}/")


def test_locked_user(page):
    credentials = test_data["locked_credentials"]
    login_obj = LoginPage(page)
    login_obj.goto_website()
    login_obj.login(credentials["username"], credentials["password"])
    expect(page.locator("[data-test='error']")).to_have_text(credentials["error"])
    expect(login_obj.login_btn).to_be_visible()
    expect(page).to_have_url(f"{BASE_URL}/")


def test_logout(valid_credentials):
    ProductPage(valid_credentials).logout()
    expect(valid_credentials).to_have_url(f"{BASE_URL}/")
    expect(LoginPage(valid_credentials).login_btn).to_be_visible()


@pytest.mark.parametrize("option", ["az", "za", "lohi", "hilo"])
def test_product_sorting(valid_credentials, option):
    products = ProductPage(valid_credentials)
    names = valid_credentials.locator("[data-test='inventory-item-name']")
    prices = valid_credentials.locator("[data-test='inventory-item-price']")
    expect(names).to_have_count(6)
    expect(prices).to_have_count(6)
    original_names = names.all_text_contents()
    original_prices = prices.all_text_contents()
    products.sort_products(option)
    expect(products.sort_select).to_have_value(option)
    if option in ("az", "za"):
        expect(names).to_have_text(sorted(original_names, reverse=option == "za"))
    else:
        expected_prices = sorted(
            original_prices,
            key=lambda price: Decimal(price.replace("$", "")),
            reverse=option == "hilo",
        )
        expect(prices).to_have_text(expected_prices)


@pytest.mark.parametrize("location", ["inventory", "cart"])
def test_remove_products(product_fixture, location):
    page = product_fixture
    products = ProductPage(page)
    cart = CartPage(page)
    if location == "cart":
        cart.open_cart()
    for index, product_id in enumerate(test_data["product_ids"]):
        if location == "cart":
            cart.remove_product(product_id)
            expect(page.locator("[data-test='inventory-item-name']")).to_have_text(
                test_data["product_names"][index + 1:]
            )
        else:
            products.remove_inventory(product_id)
            expect(page.locator(f"#add-to-cart-{product_id}")).to_be_visible()
        remaining = len(test_data["product_ids"]) - index - 1
        badge = page.locator(".shopping_cart_badge")
        if remaining:
            expect(badge).to_have_text(str(remaining))
        else:
            expect(badge).to_have_count(0)
    if location == "inventory":
        cart.open_cart()
        expect(page.locator("[data-test='inventory-item-name']")).to_have_count(0)


def test_checkout_totals(checkout_filled_fixture):
    page = checkout_filled_fixture
    expect(page).to_have_url(f"{BASE_URL}/checkout-step-two.html")
    expect(page.locator("[data-test='inventory-item-name']")).to_have_text(test_data["product_names"])
    expect(page.locator("[data-test='inventory-item-price']")).to_have_text(
        [f"${price}" for price in test_data["product_prices"]]
    )
    subtotal = sum((Decimal(price) for price in test_data["product_prices"]), Decimal("0"))
    tax = (subtotal * Decimal(test_data["tax_rate"])).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    expect(page.locator("[data-test='subtotal-label']")).to_have_text(f"Item total: ${subtotal:.2f}")
    expect(page.locator("[data-test='tax-label']")).to_have_text(f"Tax: ${tax:.2f}")
    expect(page.locator("[data-test='total-label']")).to_have_text(f"Total: ${subtotal + tax:.2f}")


def test_valid_login(valid_credentials):
    expect(valid_credentials).to_have_url(f"{BASE_URL}/inventory.html")
    expect(valid_credentials.locator("[data-test='title']")).to_have_text("Products")


def test_add_product_to_cart(product_fixture):
    expect(product_fixture.locator(".shopping_cart_badge")).to_have_text(str(len(test_data["product_ids"])))


def test_carticon_to_checkout(open_cart_fixture):
    expect(open_cart_fixture).to_have_url(f"{BASE_URL}/cart.html")
    expect(open_cart_fixture.locator("[data-test='title']")).to_have_text("Your Cart")
    expect(open_cart_fixture.locator("[data-test='inventory-item-name']")).to_have_text(test_data["product_names"])


def test_checkout(proceed_to_checkout_fixture):
    expect(proceed_to_checkout_fixture).to_have_url(f"{BASE_URL}/checkout-step-one.html")
    expect(proceed_to_checkout_fixture.locator("[data-test='title']")).to_have_text("Checkout: Your Information")
    checkout_obj = CheckoutPage(proceed_to_checkout_fixture)
    checkout_obj.checkout_proceed(test_data["checkout"]["first_name"], test_data["checkout"]["last_name"], test_data["checkout"]["zip"])
    expect(proceed_to_checkout_fixture).to_have_url(f"{BASE_URL}/checkout-step-two.html")
    expect(proceed_to_checkout_fixture.locator("[data-test='inventory-item-name']")).to_have_text(test_data["product_names"])


@pytest.mark.parametrize("first_name, last_name, zip_code, error", checkout_validation_list)
def test_checkout_form_validation(proceed_to_checkout_fixture, first_name, last_name, zip_code, error):
    expect(proceed_to_checkout_fixture).to_have_url(f"{BASE_URL}/checkout-step-one.html")
    expect(proceed_to_checkout_fixture.locator("[data-test='title']")).to_have_text("Checkout: Your Information")
    checkout_obj = CheckoutPage(proceed_to_checkout_fixture)
    checkout_obj.checkout_proceed(first_name, last_name, zip_code)
    expect(proceed_to_checkout_fixture).to_have_url(f"{BASE_URL}/checkout-step-one.html")
    expect(proceed_to_checkout_fixture.locator("[data-test='error']")).to_have_text(error)
 

def test_order_confirmation(checkout_filled_fixture):
    confirmation_obj = OrderConfirmationPage(checkout_filled_fixture)
    confirmation_obj.finish_checkout()
    expect(checkout_filled_fixture.get_by_text("Thank you for your order!")).to_be_visible()


