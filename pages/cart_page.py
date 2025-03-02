import allure
from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.__page = page
        self.__cart_quantity_label = page.locator("[data-test=\"cart-quantity-label\"]")
        self.__cart_description_label = page.locator("[data-test=\"cart-desc-label\"]")
        self.__backpack_item = page.locator("[data-test=\"item-4-title-link\"]")
        self.__t_shirt_item = page.locator("[data-test=\"item-1-title-link\"]")
        self.__t_onesie_item = page.locator("[data-test=\"item-2-title-link\"]")
        self.__remove_backpack_item_button = page.locator("[data-test=\"remove-sauce-labs-backpack\"]")
        self.__checkout_button = page.get_by_role("button", name="Checkout")
        self.__continue_shopping_button = page.get_by_role("button", name="Continue Shopping")
        self.__checkout_page_secondary_header = page.locator("[data-test=\"secondary-header\"]")

    def validate_cart_list_quantity_title(self):
        with allure.step("Validating cart list quantity title:"):
            expect(self.__cart_quantity_label).to_match_aria_snapshot("- text: QTY")

    def validate_cart_list_description_title(self):
        with allure.step("Validating cart list description title:"):
            expect(self.__cart_description_label).to_match_aria_snapshot("- text: Description")

    def validate_Sauce_Labs_Backpack_product_in_cart(self):
        with allure.step("Validating Sauce Labs Backpack is in cart:"):
            expect(self.__backpack_item).to_contain_text("Sauce Labs Backpack")

    def validate_Sauce_Labs_Bolt_T_Shirt_product_in_cart(self):
        with allure.step("ValidatingSauce Labs Bolt T-Shirt is in cart:"):
            expect(self.__t_shirt_item).to_contain_text("Sauce Labs Bolt T-Shirt")

    def validate_Sauce_Labs_Onesie_product_in_cart(self):
        with allure.step("Validating Sauce Labs Onesie is in cart:"):
            expect(self.__t_onesie_item).to_contain_text("Sauce Labs Onesie")
    #def validate_Sauce_Labs_Backpack_product_price(self):
        #with allure.step("Validating Sauce Labs Backpack price is:"):
           # expect(self.__inventory_item_price).to_contain_text("29.99")

    def validate_remove_from_cart_button_is_visible(self):
        with allure.step("Validating remove from cart button is displayed:"):
            expect(self.__remove_backpack_item_button).to_be_visible()

    def validate_checkout_button_is_visible(self):
        with allure.step("Validating checkout button is displayed:"):
            expect(self.__checkout_button).to_be_visible()

    def validate_continue_shopping_button_is_visible(self):
        with allure.step("Validating continue shopping button is displayed:"):
            expect(self.__continue_shopping_button).to_be_visible()

    def click_checkout(self):
        with allure.step("Clicking the checkout button:"):
            self.__checkout_button.click(timeout=1000)


