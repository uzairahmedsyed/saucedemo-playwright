import sys
import os
import pytest
from Pages.LoginPage import LoginPage
from Pages.ProductPage import ProductPage
from Pages.CartPage import CartPage
sys.path.insert(0, os.path.dirname(__file__))


@pytest.fixture
def valid_credentails(page):

    loginObj = LoginPage(page)
    loginObj.goto_website()
    loginObj.login("standard_user","secret_sauce")

    return page

@pytest.fixture
def product_fixture(valid_credentails):
    prodObj = ProductPage(valid_credentails)
    prodObj.add_inventory()

    return valid_credentails

@pytest.fixture
def carticon_fixture(product_fixture):
    carticonObj = CartPage(product_fixture)
    carticonObj.open_cart()
    # carticonObj.proceed_to_checkout()

    return product_fixture

@pytest.fixture
def proceed_to_checkout_fixture (carticon_fixture):
    proceed_to_checkout_obj = CartPage(carticon_fixture)
    proceed_to_checkout_obj.proceed_to_checkout()

    return carticon_fixture