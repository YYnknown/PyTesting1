from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.human_typing import slow_typing
from utils.human_delay import wait_random

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://b2c.passport.rt.ru/"
        self.wait = WebDriverWait(driver, 10)

    EMAIL_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "kc-login")
    EMAIL_TAB = (By.ID, "t-btn-tab-mail")
    ERROR_MESSAGE = (By.CLASS_NAME, "card-container__error")

    def open(self):
        self.driver.get(self.url)
        self.wait.until(EC.presence_of_element_located(self.EMAIL_INPUT))

    def switch_to_email_tab(self):
        """Переключиться на вкладку 'Почта'"""
        self.driver.find_element(*self.EMAIL_TAB).click()
        wait_random()

    def login(self, email, password):
        email_field = self.driver.find_element(*self.EMAIL_INPUT)
        email_field.clear()
        wait_random()
        slow_typing(email_field, email)

        password_field = self.driver.find_element(*self.PASSWORD_INPUT)
        password_field.clear()
        wait_random()
        slow_typing(password_field, password)

        wait_random()
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_username_required_error(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "username-meta"))
            )
            return self.driver.find_element(By.ID, "username-meta").text
        except:
            return None

    def get_login_error_message(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "form-error-message"))
            )
            return self.driver.find_element(By.ID, "form-error-message").text
        except:
            return None

    def get_error_message(self):
        return self.get_login_error_message()
