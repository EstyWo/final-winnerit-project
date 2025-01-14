import pytest
from playwright.sync_api import Page

from api_requests.users_api import UsersApi
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)

@pytest.fixture
def products_page(page: Page):
    return ProductsPage(page)

@pytest.fixture
def users_api(page: Page):
    return UsersApi(page)


