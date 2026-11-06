import re
from playwright.sync_api import Page, expect

def test_successful_login(page: Page):
    # Navigate to the standard e-commerce testing sandbox
    page.goto("https://www.saucedemo.com/")
    
    # Fill in valid credentials
    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='password']").fill("secret_sauce")
    
    # Click login button
    page.locator("[data-test='login-button']").click()
    
    # Assert successful login by checking the URL and inventory container visibility
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")