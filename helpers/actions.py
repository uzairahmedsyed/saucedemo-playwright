from playwright.sync_api import Page

BASE_URL = "https://www.saucedemo.com"


def open_site(page: Page):
    page.goto(BASE_URL)


def login_with_invalid_credentials(page: Page):
    open_site(page)
    page.get_by_placeholder("Username").fill("ABCD")
    page.get_by_placeholder("Password").fill("1234")
    page.get_by_role("button", name="Login").click()


def login_with_valid_credentials(page: Page):
    open_site(page)
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()


def add_to_cart(page: Page):
    page.locator("#add-to-cart-sauce-labs-backpack").click()


def open_cart(page: Page):
    page.locator(".shopping_cart_link").click()


def proceed_to_checkout(page: Page):
    page.get_by_role("button", name="Checkout").click()


def fill_checkout_form(page: Page):
    page.get_by_placeholder("First Name").fill("John")
    page.get_by_placeholder("Last Name").fill("Doe")
    page.get_by_placeholder("Zip/Postal Code").fill("90248")
    page.get_by_text("Continue").click()


def confirm_order(page: Page):
    page.get_by_text("Finish").click()