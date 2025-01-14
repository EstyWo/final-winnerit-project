from playwright.sync_api import Page, expect


def test_end_2_end_Scenario_A(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    expect(page.locator("[data-test=\"shopping-cart-link\"]")).to_be_visible()
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]").click()
    expect(page.locator("[data-test=\"shopping-cart-badge\"]")).to_contain_text("4")
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Your Cart")
    page.locator("[data-test=\"checkout\"]").click()

    page.locator("[data-test=\"firstName\"]").fill("alex")
    page.locator("[data-test=\"lastName\"]").fill("komanov")
    page.locator("[data-test=\"postalCode\"]").fill("20100")

    page.locator("[data-test=\"continue\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Checkout: Overview")
    expect(page.locator("[data-test=\"payment-info-label\"]")).to_be_visible()
    expect(page.locator("[data-test=\"shipping-info-label\"]")).to_be_visible()
    expect(page.locator("[data-test=\"total-info-label\"]")).to_be_visible()
    page.locator("[data-test=\"finish\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_be_visible()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Checkout: Complete!")
    expect(page.locator("[data-test=\"complete-header\"]")).to_contain_text("Thank you for your order!")
    expect(page.locator("[data-test=\"pony-express\"]")).to_be_visible()
    page.locator("[data-test=\"back-to-products\"]").click()
    page.get_by_role("button", name="Open Menu").click()
    page.locator("[data-test=\"logout-sidebar-link\"]").click()
    expect(page.locator("[data-test=\"login-container\"] div").filter(has_text="Login").first).to_be_visible()

    page.wait_for_timeout(2000)


def test_end_2_end_Scenario_B(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    expect(page.locator("[data-test=\"shopping-cart-link\"]")).to_be_visible()
    page.locator("[data-test=\"add-to-cart-sauce-labs-onesie\"]").click()
    page.locator("[data-test=\"add-to-cart-test.allthethings()-t-shirt-(red)\"]").click()

    expect(page.locator("[data-test=\"shopping-cart-badge\"]")).to_contain_text("2")
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Your Cart")
    page.locator("[data-test=\"checkout\"]").click()

    page.locator("[data-test=\"firstName\"]").fill("Esty")
    page.locator("[data-test=\"lastName\"]").fill("Wolpo")
    page.locator("[data-test=\"postalCode\"]").fill("20100")

    page.locator("[data-test=\"continue\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Checkout: Overview")
    expect(page.locator("[data-test=\"payment-info-label\"]")).to_be_visible()
    expect(page.locator("[data-test=\"shipping-info-label\"]")).to_be_visible()
    expect(page.locator("[data-test=\"total-info-label\"]")).to_be_visible()
    page.locator("[data-test=\"finish\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_be_visible()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Checkout: Complete!")
    expect(page.locator("[data-test=\"complete-header\"]")).to_contain_text("Thank you for your order!")
    expect(page.locator("[data-test=\"pony-express\"]")).to_be_visible()
    page.locator("[data-test=\"back-to-products\"]").click()
    page.get_by_role("button", name="Open Menu").click()
    page.locator("[data-test=\"logout-sidebar-link\"]").click()
    expect(page.locator("[data-test=\"login-container\"] div").filter(has_text="Login").first).to_be_visible()

    page.wait_for_timeout(2000)