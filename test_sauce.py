import pytest
from playwright.sync_api import expect
from login_page import LoginPage

@pytest.mark.parametrize("username, password", [
    ("standard_user", "bad_password"),
    ("locked_out_user", "secret_sauce")
])
def test_invalid_login(page, username, password):
    page.goto("https://www.saucedemo.com/")
    
    login_page = LoginPage(page)
    login_page.login(username, password)
    
    expect(login_page.error_message).to_be_visible()
