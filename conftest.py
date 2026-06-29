import sys
import os
import pytest
from Pages.LoginPage import LoginPage
sys.path.insert(0, os.path.dirname(__file__))

@pytest.fixture
def invalid_credentials(page):
    loginObj = LoginPage(page)
    loginObj.goto_website()
    loginObj.login("abc","secret_sauce")

    return page

@pytest.fixture
def valid_credentails(page):

    loginObj = LoginPage(page)
    loginObj.goto_website()
    loginObj.login("standard_user","secret_sauce")

    return page