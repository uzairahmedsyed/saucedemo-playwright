from playwright.sync_api import expect
from Pages.LoginPage import LoginPage
from Pages.ProductPage import ProductPage
from Pages.CartPage import CartPage
from Pages.CheckOutPage import CheckoutPage
from Pages.OrderConfirmationPage import OrderConfirmation
import pytest


### ye parametrize function banaya tha , abi isko aur smjhnaa hai
@pytest.mark.parametrize("username, password", [
    ("abc", "xyz"),
    ("abc", "secret_sauce"),
    ("standard_user", "xyz"),
    ("", ""),
])
def test_invalid_login(page, username , password):
    login = LoginPage(page)
    login.goto_website()
    login.login(username, password)
    expect(page.locator("[data-test='error']")).to_be_visible()


def test_valid_login(valid_credentails):
    expect(valid_credentails).to_have_url("https://www.saucedemo.com/inventory.html")

def test_add_product_to_cart( product_fixture):
    expect(product_fixture.locator(".shopping_cart_badge")).to_have_text("1")

def test_carticon_to_checkout(carticon_fixture):
    expect(carticon_fixture).to_have_url("https://www.saucedemo.com/cart.html")

def test_checkout(proceed_to_checkout_fixture):
    expect(proceed_to_checkout_fixture).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
    checkout = CheckoutPage(proceed_to_checkout_fixture)
    checkout.checkout_proceed()

def test_order_confirmation(proceed_to_checkout_fixture):
    checkout = CheckoutPage(proceed_to_checkout_fixture)
    checkout.checkout_proceed()
    confirmation = OrderConfirmation(proceed_to_checkout_fixture)
    confirmation.finish_checkout()
    expect(proceed_to_checkout_fixture.get_by_text("Thank you for your order!")).to_be_visible()


