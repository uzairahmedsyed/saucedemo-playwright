from playwright.sync_api import expect
from Pages.LoginPage import LoginPage
from Pages.CheckoutPage import CheckoutPage
from Pages.OrderConfirmationPage import OrderConfirmationPage
import pytest
import json

with open("Data/test_data.json") as f:
    test_data = json.load(f)

 
invalid_credentials_list = []
for credential in test_data["invalid_credentials"]:
    invalid_credentials_list.append((credential["username"],credential["password"]))


checkout_validation_list = []
for cred in test_data["checkout_validation"]:
    checkout_validation_list.append((cred["first_name"], cred["last_name"], cred["zip"], cred["error"]))


@pytest.mark.parametrize("username, password", invalid_credentials_list)
def test_invalid_login(page, username, password):
    login_obj = LoginPage(page)
    login_obj.goto_website()
    login_obj.login(username, password)
    expect(page.locator("[data-test='error']")).to_be_visible()


def test_valid_login(valid_credentials):
    expect(valid_credentials).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(valid_credentials.locator("[data-test='title']")).to_have_text("Products")


def test_add_product_to_cart(product_fixture):
    expect(product_fixture.locator(".shopping_cart_badge")).to_have_text(str(len(test_data["product_ids"])))


def test_carticon_to_checkout(open_cart_fixture):
    expect(open_cart_fixture).to_have_url("https://www.saucedemo.com/cart.html")
    expect(open_cart_fixture.locator("[data-test='title']")).to_have_text("Your Cart")
    expect(open_cart_fixture.locator("[data-test='inventory-item-name']")).to_have_text(test_data["product_names"])


def test_checkout(proceed_to_checkout_fixture):
    expect(proceed_to_checkout_fixture).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
    checkout_obj = CheckoutPage(proceed_to_checkout_fixture)
    checkout_obj.checkout_proceed(test_data["checkout"]["first_name"], test_data["checkout"]["last_name"], test_data["checkout"]["zip"])
    expect(proceed_to_checkout_fixture).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
    expect(proceed_to_checkout_fixture.locator("[data-test='inventory-item-name']")).to_have_text(test_data["product_names"])


@pytest.mark.parametrize("first_name, last_name, zip_code, error", checkout_validation_list)
def test_checkout_form_validation(proceed_to_checkout_fixture, first_name, last_name, zip_code, error):
    expect(proceed_to_checkout_fixture).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
    checkout_obj = CheckoutPage(proceed_to_checkout_fixture)
    checkout_obj.checkout_proceed(first_name, last_name, zip_code)
    expect(proceed_to_checkout_fixture.locator("[data-test='error']")).to_have_text(error)
 

def test_order_confirmation(checkout_filled_fixture):
    confirmation_obj = OrderConfirmationPage(checkout_filled_fixture)
    confirmation_obj.finish_checkout()
    expect(checkout_filled_fixture.get_by_text("Thank you for your order!")).to_be_visible()


