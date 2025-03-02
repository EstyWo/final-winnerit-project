import pytest
from playwright.sync_api import Page


from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)

@pytest.fixture
def products_page(page: Page):
    return ProductsPage(page)

@pytest.fixture
def cart_page(page: Page):
    return CartPage(page)

@pytest.fixture
def checkout_page(page: Page):
    return CheckoutPage(page)