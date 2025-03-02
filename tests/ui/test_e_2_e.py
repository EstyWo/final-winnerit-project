from asyncio import timeout

import allure
import pytest
from allure_commons.types import AttachmentType
from playwright.sync_api import Page, expect
from utils import configs


@allure.feature("Login")
@allure.story("E2E Test Scenario A & B")
@allure.title("E2E Test")

    # collect 3 items, find them in cart page, and finish checkout
def test_e2e_scenario_a(page: Page, login_page, products_page, cart_page, checkout_page):
    # login to the platform with visual_user details
    login_page.navigate_to(configs.base_url)
    login_page.login_to_application(configs.standard_user, configs.correct_password)

    # moving to products page, collecting products
    login_page.validate_page_url(configs.base_url + 'inventory.html')
    allure.attach(page.screenshot(full_page=True), name="screenshot", attachment_type=AttachmentType.PNG)
    page.wait_for_timeout(3000)

    # validate headers & shopping cart are in the products page
    products_page.validate_primary_header_aria_snapshot()
    products_page.validate_secondary_header_aria_snapshot()
    products_page.validate_shopping_cart_is_visible()

    # adding 3 products to the cart
    products_page.add_to_cart_Backpack()
    products_page.add_to_cart_T_shirt()
    products_page.add_to_cart_Onesie()

    # validate items in cart and move to shopping cart page
    products_page.validate_items_in_cart()
    products_page.moving_to_shopping_cart_page()
    products_page.validate_page_url(configs.base_url + 'cart.html')

    #checking the cart page, validate that there are products in cart
    cart_page.validate_cart_list_quantity_title()
    cart_page.validate_cart_list_description_title()
    cart_page.validate_Sauce_Labs_Backpack_product_in_cart()
    cart_page.validate_Sauce_Labs_Bolt_T_Shirt_product_in_cart()
    cart_page.validate_remove_from_cart_button_is_visible()
    cart_page.validate_checkout_button_is_visible()
    cart_page.validate_continue_shopping_button_is_visible()
    cart_page.click_checkout()
    cart_page.validate_page_url(configs.base_url + 'checkout-step-one.html')

    #checking the checkout page, filling the user fist name & last name & zip code
    checkout_page.validate_continue_button_is_visible()
    checkout_page.validate_cancel_button_is_visible()
    checkout_page.fill_in_user_details(configs.first_name, configs.last_name, configs.zip_code)
    checkout_page.validate_cancel_button_is_visible()
    checkout_page.click_finish()
    checkout_page.validate_checkout_complete_message_display()
    checkout_page.logout_app()
    checkout_page.validate_login_page_displayed()

    # add 3 items to cart, continue checkout,
    # then go back and remove 1 item,
    # then validate the total price and finish

def test_e2e_scenario_b(page: Page, login_page, products_page, cart_page, checkout_page):
    #login to the platform with visual_user details
    login_page.navigate_to(configs.base_url)
    login_page.login_to_application(configs.visual_user, configs.correct_password)

    # moving to products page, collecting products
    login_page.validate_page_url(configs.base_url + 'inventory.html')
    allure.attach(page.screenshot(full_page=True), name="screenshot", attachment_type=AttachmentType.PNG)
    page.wait_for_timeout(3000)

    # validate headers & shopping cart are in the products page
    products_page.validate_primary_header_aria_snapshot()
    products_page.validate_secondary_header_aria_snapshot()
    products_page.validate_shopping_cart_is_visible()

    # adding 3 products to the cart
    products_page.add_to_cart_Backpack()
    products_page.add_to_cart_T_shirt()
    products_page.add_to_cart_Onesie()

    #validate items in cart and move to shopping cart page
    products_page.validate_items_in_cart()
    products_page.moving_to_shopping_cart_page()
    products_page.validate_page_url(configs.base_url + 'cart.html')

    #checking the cart page, validate that the items products in cart
    cart_page.validate_cart_list_quantity_title()
    cart_page.validate_cart_list_description_title()
    cart_page.validate_Sauce_Labs_Backpack_product_in_cart()
    cart_page.validate_Sauce_Labs_Bolt_T_Shirt_product_in_cart()
    cart_page.validate_Sauce_Labs_Onesie_product_in_cart()

    #rvalidate that remove item, checkout & continue buttons are displayed
    cart_page.validate_remove_from_cart_button_is_visible()
    cart_page.validate_checkout_button_is_visible()
    cart_page.validate_continue_shopping_button_is_visible()
    cart_page.click_checkout()
    cart_page.validate_page_url(configs.base_url + 'checkout-step-one.html')

    #checking the checkout page, filling the user fist name & last name & zip code
    checkout_page.validate_continue_button_is_visible()
    checkout_page.validate_cancel_button_is_visible()
    checkout_page.fill_in_user_details(configs.first_name, configs.last_name, configs.zip_code)

    #validate that the total price of 3 items is 53.97
    checkout_page.validate_total_some_items_price(configs.total_3_price)

    #click cancel in order to move back to shopping cart
    checkout_page.click_cancel()

    #remote item from the cart and continue
    products_page.remove_Tshirt_from_cart()
    products_page.moving_to_shopping_cart_page()
    cart_page.click_checkout()
    checkout_page.fill_in_user_details(configs.first_name, configs.last_name, configs.zip_code)

    #check the price of the items in cart
    onesie_price = checkout_page.get_onesie_price(configs.onesie_price)
    backpack_price = checkout_page.get_backpack_price(configs.backpack_price)

    #check the current total items price
    price_2_items = checkout_page.validate_total_some_items_price(configs.total_2_price)


    assert price_2_items == onesie_price + backpack_price


    checkout_page.click_finish()
    checkout_page.validate_checkout_complete_message_display()
    checkout_page.logout_app()
    checkout_page.validate_login_page_displayed()

    allure.attach(page.screenshot(full_page=True), name="screenshot", attachment_type=AttachmentType.PNG)
    page.wait_for_timeout(2000)