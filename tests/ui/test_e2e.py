from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_standard_user_login(browser):
    login_page = LoginPage(browser)

    # Navigation to the app
    login_page.open_home_page()

    # Filling Form
    login_page.type_username("standard_user")
    login_page.type_password('secret_sauce')
    login_page.click_login_button()

    # Validation of redirection
    inventory_page = InventoryPage(browser=browser)
    inventory_page.validation_inventory_page_title()
    inventory_page.validation_inventory_page_url()

    # Add products to the cart
    inventory_page.add_to_cart_backpack()
    shopping_cart_item = inventory_page.get_shopping_cart_badge()
    assert shopping_cart_item == 1

    inventory_page.add_to_cart_bike_light()
    shopping_cart_item = inventory_page.get_shopping_cart_badge()
    assert shopping_cart_item == 2

    inventory_page.remove_bike_light()
    shopping_cart_item = inventory_page.get_shopping_cart_badge()
    assert shopping_cart_item == 1

    inventory_page.sort_item()