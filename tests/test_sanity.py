import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture(scope="function")

def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login_valid_inputs(driver):
    login_page = LoginPage(driver)
    login_page.navigate()
    login_page.enter_username('testuser')
    login_page.enter_password('testpass')
    login_page.click_login()
    assert "dashboard" in driver.current_url,"Login with valid inputs failed"

def test_login_invalid_inputs(driver):
    login_page = LoginPage(driver)
    login_page.navigate()
    login_page.enter_username('wrongtester')
    login_page.enter_password('wrongpass')
    login_page.click_login()
    assert "login" in driver.current_url, "Login with invalid inputs should fail"
    


