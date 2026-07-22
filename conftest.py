import sys
import os
import pytest
from Pages.LoginPage import LoginPage
from Pages.ProductPage import ProductPage
from Pages.CartPage import CartPage
sys.path.insert(0, os.path.dirname(__file__))
import json

with open("Data/test_data.json") as load_json_file:
    test_data = json.load(load_json_file)
    
@pytest.fixture
def valid_credentials(page):
    login_obj = LoginPage(page)
    login_obj.goto_website()
    login_obj.login(test_data["valid_credentials"]["username"],test_data["valid_credentials"]["password"])

    return page

@pytest.fixture
def product_fixture(valid_credentials):
    prod_obj = ProductPage(valid_credentials)
    prod_obj.add_inventory(test_data["product_ids"][0])
    prod_obj.add_inventory(test_data["product_ids"][1])                           

    return valid_credentials

@pytest.fixture
def open_cart_fixture(product_fixture):
    carticon_obj = CartPage(product_fixture)
    carticon_obj.open_cart()

    return product_fixture

@pytest.fixture
def proceed_to_checkout_fixture(open_cart_fixture):
    proceed_to_checkout_obj = CartPage(open_cart_fixture)
    proceed_to_checkout_obj.proceed_to_checkout()

    return open_cart_fixture