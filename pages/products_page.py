import allure
from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class ProductsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.__page = page
        self.__primary_header = page.locator("[data-test=\"primary-header\"]")
        self.__secondary_header = page.locator("[data-test=\"secondary-header\"]")
        self.__shopping_cart_link = page.locator("[data-test=\"shopping-cart-link\"]")
        self.__add_to_cart_button_Backpack = page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")
        self.__add_to_cart_button_T_shirt = page.locator("[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]")
        self.__add_to_cart_button_Onesie = page.locator("[data-test=\"add-to-cart-sauce-labs-onesie\"]")
        self.__remove_from_cart_button_TShirt = page.locator("[data-test=\"remove-sauce-labs-bolt-t-shirt\"]")
        self.__shopping_cart = page.locator("[data-test=\"shopping-cart-badge\"]")
        self.__shopping_cart_link = page.locator("[data-test=\"shopping-cart-link\"]")

    def validate_primary_header_aria_snapshot(self):
        with allure.step("Validating primary header area:"):
            expect(self.__primary_header).to_match_aria_snapshot("- text: Swag Labs")

    def validate_secondary_header_aria_snapshot(self):
        with allure.step("Validating primary header area:"):
            expect(self.__secondary_header).to_match_aria_snapshot(
            "- text: Products Name (A to Z)\n- combobox:\n  - option \"Name (A to Z)\" [selected]\n  - option \"Name (Z to A)\"\n  - option \"Price (low to high)\"\n  - option \"Price (high to low)\"")

    def validate_shopping_cart_is_visible(self):
        with allure.step("Validating shopping cart is visible:"):
            expect(self.__shopping_cart_link).to_be_visible()

    def add_to_cart_Backpack(self):
        with allure.step("Adding Backpack to cart:"):
            self.__add_to_cart_button_Backpack.click()

    def add_to_cart_T_shirt(self):
                with allure.step("Adding T-shirt to cart:"):
                    self.__add_to_cart_button_T_shirt.click()

    def add_to_cart_Onesie(self):
                with allure.step("Adding Onesie to cart:"):
                    self.__add_to_cart_button_Onesie.click()

    def validate_items_in_cart(self):
        with allure.step("Validating there are 3 items in cart:"):
            expect(self.__shopping_cart).to_contain_text("3")

    def remove_Tshirt_from_cart(self):
        with allure.step("Removing T-Shirt from cart:"):
            self.__remove_from_cart_button_TShirt.click()

    def validate_items_in_cart_after_remove(self):
        with allure.step("Validating num of items after remove item:"):
            expect(self.__shopping_cart).to_contain_text("2")

    def moving_to_shopping_cart_page(self):
        with allure.step("Moving to shopping cart page"):
            self.__shopping_cart_link.click(timeout=60000)


