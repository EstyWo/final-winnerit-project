from time import sleep
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By

class InventoryPage:

    def __init__(self, browser):
        self.browser = browser

    def validation_inventory_page_title(self, expected_title = 'Products'):
        inventory_page_title = self.browser.find_element(By.XPATH, value='//*[@data-test="title"]').text
        print(f"{inventory_page_title = }")
        assert inventory_page_title == "Products"

    def validation_inventory_page_url(self):
        current_url = self.browser.current_url
        print(f"{current_url = }")
        assert current_url == "https://www.saucedemo.com/inventory.html"

    def add_to_cart_backpack(self):
        sauce_labs_backpack = self.browser.find_element(By.NAME, value="add-to-cart-sauce-labs-backpack").click()

    def add_to_cart_bike_light(self):
        sauce_labs_bike_light = self.browser.find_element(By.NAME, value="add-to-cart-sauce-labs-bike-light").click()

    def add_to_cart_bolt_t_shirt(self):
        sauce_labs_bolt_t_shirt = self.browser.find_element(By.NAME, value="add-to-cart-sauce-labs-bolt-t-shirt").click()

    def add_to_cart_fleece_jacket(self):
        sauce_labs_bike_light = self.browser.find_element(By.NAME, value="add-to-cart-sauce-labs-fleece-jacket").click()

    def add_to_cart_onesie(self):
        sauce_Labs_onesie = self.browser.find_element(By.NAME, value="add-to-cart-sauce-labs-onesie").click()

    def remove_bike_light(self):
        remove_bike_light = self.browser.find_element(By.NAME, value="remove-sauce-labs-backpack").click()

    def get_shopping_cart_badge(self):
        shopping_cart_badge = self.browser.find_element(By.CLASS_NAME, value="shopping_cart_badge")
        print (shopping_cart_badge.text)
        return shopping_cart_badge.text

    def sort_item(self):
        product_sort_container = self.browser.find_element(By.CLASS_NAME, value="product_sort_container")
        product_sort_container.click()
        sleep(5)
        print("line 48")
        print (product_sort_container.text)
        product_sort_container.send_keys("Price (low to high)")
        print("line 51")
        product_sort_container.click()
        off_click = self.browser.find_element(By.ID, value="inventory_container").click()





