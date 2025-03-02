import allure
import pytest
from allure_commons.types import AttachmentType
from playwright.sync_api import Page, expect
from utils import configs

user_name_list= [configs.standard_user, configs.performance_glitch_user, configs.error_user, configs.visual_user]
@allure.feature("Login")
@allure.story("Happy Scenarios")
@allure.title("4 Happy Scenarios Tests")
@pytest.mark.parametrize("user_name", user_name_list)
def test_success_login(page: Page, login_page, user_name):
    login_page.navigate_to(configs.base_url)
    login_page.login_to_application(user_name, configs.correct_password)
    login_page.validate_page_url(configs.base_url + 'inventory.html')
    allure.attach(page.screenshot(full_page=True), name="screenshot", attachment_type=AttachmentType.PNG)
    page.wait_for_timeout(3000)
