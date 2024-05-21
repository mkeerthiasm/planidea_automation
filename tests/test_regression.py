import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login_logout_regression(driver):
    login_page = LoginPage(driver)
    login_page.navigate()
    login_page.enter_username('testuser')
    login_page.enter_password('testpass')
    assert "dashboard" in driver.current_url, "Login failed"
    login_page.logout()
    assert "login" in driver.current_url, "Logout failed"    