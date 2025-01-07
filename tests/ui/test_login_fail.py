from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

# test the case when filling locked user details
def test_locked_out_user_login(browser):
    login_page = LoginPage(browser)

    # Navigation to the app
    login_page.open_home_page()

    # Filling Form
    login_page.type_username("locked_out_user")
    login_page.type_password('secret_sauce')
    login_page.click_login_button()

    # Validation of Error message
    error_message_text = browser.find_element(By.CSS_SELECTOR, value='[data-test="error"]').text
    print(f"{error_message_text = }")
    assert error_message_text == "Epic sadface: Sorry, this user has been locked out."

# test the case when the username is not from the list
def test_invalid_user_login(browser):
    login_page = LoginPage(browser)

    # Navigation to the app
    login_page.open_home_page()

    # Filling Form
    login_page.type_username("invalid_user")
    login_page.type_password('secret_sauce')
    login_page.click_login_button()

    # Validation of Error message
    error_message_text = browser.find_element(By.CSS_SELECTOR, value='[data-test="error"]').text
    print(f"{error_message_text = }")
    assert error_message_text == "Epic sadface: Username and password do not match any user in this service"

# test the case when the user field is blank
def test_blank_user_login(browser):
    login_page = LoginPage(browser)

    # Navigation to the app
    login_page.open_home_page()

    # Filling only password field
    login_page.type_password('secret_sauce')
    login_page.click_login_button()

    # Validation of Error message
    error_message_text = browser.find_element(By.CSS_SELECTOR, value='[data-test="error"]').text
    print(f"{error_message_text = }")
    assert error_message_text == "Epic sadface: Username is required"

# test the case when the password field is blank
def test_blank_password_login(browser):
    login_page = LoginPage(browser)

    # Navigation to the app
    login_page.open_home_page()

    # Filling only username field
    login_page.type_username("invalid_user")
    login_page.click_login_button()

    # Validation of Error message
    error_message_text = browser.find_element(By.CSS_SELECTOR, value='[data-test="error"]').text
    print(f"{error_message_text = }")
    assert error_message_text == "Epic sadface: Password is required"