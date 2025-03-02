import allure
from allure_commons.types import AttachmentType
from playwright.sync_api import Page, expect
import pytest

from utils import configs

test_data = [
    (configs.locked_out_user, configs.correct_password, "Epic sadface: Sorry, this user has been locked out."),
    ("test_user", "secret_sauce", "Epic sadface: Username and password do not match any user in this service"),
    ("", configs.correct_password, "Epic sadface: Username is required"),
    ("test_user", "", "Epic sadface: Password is required")
]


@allure.feature("Login")
@allure.story("Negative Scenarios")
@allure.title("4 Negative Scenario Tests")
@pytest.mark.parametrize("user_name, password, error_message",test_data)
def test_negative_scenarios(page: Page, login_page, user_name, password, error_message):
    login_page.navigate_to(configs.base_url)
    login_page.login_to_application(user_name, password)
    login_page.validate_error_message(error_message)
    login_page.validate_page_url(configs.base_url)
    allure.attach(page.screenshot(full_page=True), name="screenshot", attachment_type=AttachmentType.PNG)
    page.wait_for_timeout(2000)
