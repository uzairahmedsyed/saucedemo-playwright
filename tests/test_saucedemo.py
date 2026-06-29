from playwright.sync_api import expect
# from Pages.LoginPage import LoginPage
from Pages.ProductPage import ProductPage
from Pages.CartPage import CartPage
from Pages.CheckOutPage import CheckoutPage
from Pages.OrderConfirmationPage import OrderConfirmation


def test_invalid_login(invalid_credentials):
    # login = LoginPage(invalid_credentials)
    # login.goto_website()
    # login.login("Abc", "XYZ")
    expect(invalid_credentials.locator("[data-test='error']")).to_be_visible()

def test_valid_login(valid_credentails):
    # login = LoginPage(page)
    # login.goto_website()
    # login.login("standard_user", "secret_sauce")
    expect(valid_credentails).to_have_url("https://www.saucedemo.com/inventory.html")

def test_add_product_to_cart(valid_credentails):
    # login = LoginPage(page)
    # login.goto_website()
    # login.login("standard_user", "secret_sauce")
    product = ProductPage(valid_credentails)
    product.add_inventory()
    expect(valid_credentails.locator(".shopping_cart_badge")).to_have_text("1")

def test_carticon_to_checkout(valid_credentails):
    # login = LoginPage(page)
    # login.goto_website()
    # login.login("standard_user", "secret_sauce")
    product = ProductPage(valid_credentails)
    product.add_inventory()
    cart = CartPage(valid_credentails)
    cart.open_cart()
    expect(valid_credentails).to_have_url("https://www.saucedemo.com/cart.html")
    cart.proceed_to_checkout()

def test_checkout(valid_credentails):
    # login = LoginPage(page)
    # login.goto_website()
    # login.login("standard_user", "secret_sauce")
    product = ProductPage(valid_credentails)
    product.add_inventory()
    cart = CartPage(valid_credentails)
    cart.open_cart()
    cart.proceed_to_checkout()
    expect(valid_credentails).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
    checkout = CheckoutPage(valid_credentails)
    checkout.checkout_proceed()

def test_order_confirmation(valid_credentails):
    # login = LoginPage(page)
    # login.goto_website()
    # login.login("standard_user", "secret_sauce")
    product = ProductPage(valid_credentails)
    product.add_inventory()
    cart = CartPage(valid_credentails)
    cart.open_cart()
    cart.proceed_to_checkout()
    # expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
    checkout = CheckoutPage(valid_credentails)
    checkout.checkout_proceed()
    confirmation = OrderConfirmation(valid_credentails)
    confirmation.finish_checkout()
    expect(valid_credentails.get_by_text("Thank you for your order!")).to_be_visible()


