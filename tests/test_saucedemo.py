from playwright.sync_api import expect
from helpers.actions import (
    login_with_invalid_credentials,
    login_with_valid_credentials,
    add_to_cart,
    open_cart,
    proceed_to_checkout,
    fill_checkout_form,
    confirm_order,
)

BASE_URL = "https://www.saucedemo.com"


def test_invalid_login(page):
    login_with_invalid_credentials(page)
    expect(page.locator("[data-test='error']")).to_be_visible()


def test_valid_login(page):
    login_with_valid_credentials(page)
    expect(page).to_have_url(f"{BASE_URL}/inventory.html")


def test_add_to_cart(page):
    login_with_valid_credentials(page)
    add_to_cart(page)
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")


def test_open_cart(page):
    login_with_valid_credentials(page)
    add_to_cart(page)
    open_cart(page)
    expect(page).to_have_url(f"{BASE_URL}/cart.html")


def test_proceed_to_checkout(page):
    login_with_valid_credentials(page)
    add_to_cart(page)
    open_cart(page)
    proceed_to_checkout(page)
    expect(page).to_have_url(f"{BASE_URL}/checkout-step-one.html")


def test_fill_checkout_form(page):
    login_with_valid_credentials(page)
    add_to_cart(page)
    open_cart(page)
    proceed_to_checkout(page)
    fill_checkout_form(page)
    expect(page).to_have_url(f"{BASE_URL}/checkout-step-two.html")


def test_confirm_order(page):
    login_with_valid_credentials(page)
    add_to_cart(page)
    open_cart(page)
    proceed_to_checkout(page)
    fill_checkout_form(page)
    confirm_order(page)
    expect(page.get_by_text("Thank you for your order")).to_be_visible()