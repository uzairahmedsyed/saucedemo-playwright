from playwright.sync_api import expect
from Pages.LoginPage import LoginPage
from Pages.ProductPage import ProductPage
from Pages.CartPage import CartPage
from Pages.CheckOutPage import CheckoutPage
from Pages.OrderConfirmationPage import OrderConfirmation


def test_invalid_login(page):
    login = LoginPage(page)
    login.goto_website()
    login.login("Abc", "XYZ")
    expect(page.locator("[data-test='error']")).to_be_visible()

def test_valid_login(page):
    login = LoginPage(page)
    login.goto_website()
    login.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_add_product_to_cart(page):
    login = LoginPage(page)
    login.goto_website()
    login.login("standard_user", "secret_sauce")
    product = ProductPage(page)
    product.add_Inventory()
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")

def test_carticon_to_checkout(page):
    login = LoginPage(page)
    login.goto_website()
    login.login("standard_user", "secret_sauce")
    product = ProductPage(page)
    product.add_Inventory()
    cart = CartPage(page)
    cart.open_cart()
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    cart.proceed_to_checkout()

def test_checkout(page):
    login = LoginPage(page)
    login.goto_website()
    login.login("standard_user", "secret_sauce")
    product = ProductPage(page)
    product.add_Inventory()
    cart = CartPage(page)
    cart.open_cart()
    cart.proceed_to_checkout()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
    checkout = CheckoutPage(page)
    checkout.checkout_proceed()

def test_order_confirmation(page):
    login = LoginPage(page)
    login.goto_website()
    login.login("standard_user", "secret_sauce")
    product = ProductPage(page)
    product.add_Inventory()
    cart = CartPage(page)
    cart.open_cart()
    cart.proceed_to_checkout()
    # expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
    checkout = CheckoutPage(page)
    checkout.checkout_proceed()
    confirmation = OrderConfirmation(page)
    confirmation.finish_checkout()
    expect(page.get_by_text("Thank you for your order!")).to_be_visible()