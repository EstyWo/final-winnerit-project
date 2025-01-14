from playwright.sync_api import Page, expect


def test_standard_user(page: Page):
    base_url = "https://www.saucedemo.com/"
    page.goto(base_url)
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    expect(page).to_have_url(base_url + 'inventory.html')
    page.wait_for_timeout(2000)

def test_performance_glitch_user(page: Page):
    base_url = "https://www.saucedemo.com/"
    page.goto(base_url)
    page.locator("[data-test=\"username\"]").fill("performance_glitch_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    expect(page).to_have_url(base_url + 'inventory.html')
    page.wait_for_timeout(2000)

def test_error_user(page: Page):
    base_url = "https://www.saucedemo.com/"
    page.goto(base_url)
    page.locator("[data-test=\"username\"]").fill('error_user')
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    expect(page).to_have_url(base_url + 'inventory.html')
    page.wait_for_timeout(2000)

def test_visual_user(page: Page):
    base_url = "https://www.saucedemo.com/"
    page.goto(base_url)
    page.locator("[data-test=\"username\"]").fill("visual_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    expect(page).to_have_url(base_url + 'inventory.html')
    page.wait_for_timeout(2000)