from selenium.webdriver.common.by import By
from .base_page.py import BasePage

class LoginPage(BasePage):
    URL = 'https://planidea.netlify.app/login'

    def navigate(self):
        self.driver.get(self.URL)

    def enter_username(self, username):
        username_field = self.wait_for_element(By.ID, 'username')
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.wait_for_element(By.ID, 'password')
        password_field.send_keys(password)

    def click_login(self):
        login_button = self.wait_for_element(By.ID, 'login_button')
        login_button.click()

    def logout(self):
        logout_button = self.wait_for_element(By.ID, 'logout_button')
        logout_button.click()            
            
