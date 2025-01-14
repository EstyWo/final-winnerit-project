from playwright.sync_api import Page, expect


def test_negative_scenarios(page: Page):
    base_url = "https://www.saucedemo.com/"
    page.goto(base_url)
    page.locator("[data-test=\"username\"]").fill("locked_out_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    expect(page.locator("[data-test=\"error\"]")).to_contain_text("Epic sadface: Sorry, this user has been locked out.")
    expect(page).to_have_url(base_url)
    page.wait_for_timeout(2000)

def test_user_not_found_scenarios(page: Page):
    base_url = "https://www.saucedemo.com/"
    page.goto(base_url)
    page.locator("[data-test=\"username\"]").fill("test_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    expect(page.locator("[data-test=\"error\"]")).to_contain_text("Epic sadface: Username and password do not match any user in this service")
    expect(page).to_have_url(base_url)
    page.wait_for_timeout(2000)

def test_user_field_empty_scenarios(page: Page):
    base_url = "https://www.saucedemo.com/"
    page.goto(base_url)
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    expect(page.locator("[data-test=\"error\"]")).to_contain_text("Epic sadface: Username is required")
    expect(page).to_have_url(base_url)
    page.wait_for_timeout(2000)

def test_password_field_empty_scenarios(page: Page):
    base_url = "https://www.saucedemo.com/"
    page.goto(base_url)
    page.locator("[data-test=\"username\"]").fill("test_user")
    page.locator("[data-test=\"login-button\"]").click()
    expect(page.locator("[data-test=\"error\"]")).to_contain_text("Epic sadface: Password is required")
    expect(page).to_have_url(base_url)
    page.wait_for_timeout(2000)