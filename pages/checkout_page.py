from contextlib import nullcontext
from itertools import product

import allure
from playwright.sync_api import Page, expect


from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.__page = page
        #self.__checkout_title =  page.locator("[data-test=\"title\"]")
        self.__firstname_textfield = page.get_by_placeholder("First Name")
        self.__lastname_textfield = page.get_by_placeholder("Last Name")
        self.__zipcode_textfield = page.get_by_placeholder("Zip/Postal Code")
        self.__cancel_button = page.get_by_role("button", name="Cancel")
        self.__continue_button = page.get_by_role("button", name="Continue")
        self.__payment_info_value = page.locator("[data-test=\"payment-info-value\"]")
        self.__shipping_info_label = page.locator("[data-test=\"shipping-info-label\"]")

        self.__onesie_item = page.locator("[class=\"cart_item_label\"]",has_text="Sauce Labs Onesie")
        self.__backpack_item = page.locator("[class=\"cart_item_label\"]", has_text="Sauce Labs Backpack")

        self.__total_price = page.locator("[data-test=\"total-label\"]")

        self.__finish_button = page.get_by_role("button", name="Finish")
        self.__checkout_complete_message = page.locator("[data-test=\"complete-header\"]")
        self.__back_home_button = page.get_by_role("button", name="Back Home")
        self.__open_menu = page.get_by_role("button", name="Open Menu")
        self.__logout = page.locator("[data-test=\"logout-sidebar-link\"]")
        self.__login_button = page.get_by_role("button", name="Login")
        self.__subtotal_price = page.locator("[data-test=\"subtotal-label\"]")

    # def validate_checkout_title(self):
    #     with allure.step("Validating cart list quantity title:"):
    #         expect(self.__checkout_title).to_match_aria_snapshot("- text: Checkout: Your Information")

    def validate_continue_button_is_visible(self):
        with allure.step("Validating continue button is displayed:"):
            expect(self.__continue_button).to_be_visible()

    def validate_cancel_button_is_visible(self):
        with allure.step("Validating cancel button is displayed:"):
            expect(self.__cancel_button).to_be_visible()

    def fill_in_user_details(self, firstname: str, lastname: str, zipcode: str):
        with allure.step(f"Fill in user details: {firstname} : {lastname}"):
            self.__firstname_textfield.fill(firstname, timeout=60000)
            self.__lastname_textfield.fill(lastname, timeout=60000)
            self.__zipcode_textfield.fill(zipcode, timeout=60000)
            self.__continue_button.click()

    def click_finish(self):
        with allure.step("Clicking the finish button:"):
            self.__finish_button.click()

    def click_cancel(self):
        with allure.step("Clicking the cancel button:"):
            self.__cancel_button.click()

    def get_onesie_price(self, price:str):
        with allure.step("get sauce in page:"):
            expect(self.__onesie_item).to_contain_text(price)
            return float(self.__onesie_item.inner_text()[-4:])

    def get_backpack_price(self, price:str):
        with allure.step("get backpack in page:"):
            expect(self.__backpack_item).to_contain_text(price)
            return float(self.__backpack_item.inner_text()[-5:])

    def validate_total_some_items_price(self, price:str):
        with allure.step("Validate total item price:"):
            expect(self.__subtotal_price).to_contain_text(price)
            return float(self.__subtotal_price.inner_text()[-5:])


    def validate_checkout_complete_message_display(self):
        with allure.step("Validating checkout complete message is displayed:"):
            expect(self.__checkout_complete_message).to_contain_text("Thank you for your order!")

    def validate_back_home_button_is_visible(self):
        with allure.step("Validating Back Home button is displayed:"):
            expect(self.__back_home_button).to_be_visible()

    def logout_app(self):
        with allure.step("Logout the app"):
            self.__open_menu.click()
            self.__logout.click()

    def validate_login_page_displayed(self):
            with allure.step("Validating Login page is displayed:"):
                expect(self.__login_button).to_be_visible()





