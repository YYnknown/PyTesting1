from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.human_typing import slow_typing
from utils.human_delay import wait_random


class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://b2c.passport.rt.ru/"
        self.wait = WebDriverWait(driver, 10)

    # --- Локаторы ---
    FIRST_NAME = (By.NAME, "firstName")
    LAST_NAME = (By.NAME, "lastName")
    REGION_INPUT = (By.CSS_SELECTOR, "input.rt-select__input")
    EMAIL_INPUT = (By.ID, "address")
    PASSWORD_INPUT = (By.ID, "password")
    CONFIRM_PASSWORD_INPUT = (By.ID, "password-confirm")

    REGISTER_BUTTON = (By.NAME, "register")
    BACK_TO_LOGIN_BUTTON = (By.ID, "reset-back")
    AGREEMENT_LINK = (By.ID, "rt-auth-agreement-link")
    HELP_LINK = (By.LINK_TEXT, "Помощь")

    REGISTER_LINK = (By.LINK_TEXT, "Зарегистрироваться")
    ERROR_MESSAGES = (By.CLASS_NAME, "rt-input-container__meta--error")

    # --- Методы ---

    def open(self):
        self.driver.get(self.url)
        self.wait.until(EC.element_to_be_clickable(self.REGISTER_LINK)).click()
        self.wait.until(EC.presence_of_element_located(self.FIRST_NAME))
        wait_random()

    def enter_first_name(self, name):
        field = self.driver.find_element(*self.FIRST_NAME)
        field.clear()
        wait_random()
        slow_typing(field, name)
        wait_random()

    def enter_last_name(self, lastname):
        field = self.driver.find_element(*self.LAST_NAME)
        field.clear()
        wait_random()
        slow_typing(field, lastname)
        wait_random()

    def select_region_by_index(self, index=0):
        self.driver.find_element(*self.REGION_INPUT).click()
        wait_random()
        options = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'rt-select__list')]/div")
        if options and index < len(options):
            options[index].click()
            wait_random()

    def enter_email(self, email):
        field = self.driver.find_element(*self.EMAIL_INPUT)
        field.clear()
        wait_random()
        slow_typing(field, email)
        wait_random()

    def enter_password(self, password):
        field = self.driver.find_element(*self.PASSWORD_INPUT)
        field.clear()
        wait_random()
        slow_typing(field, password)
        wait_random()

    def enter_confirm_password(self, password):
        field = self.driver.find_element(*self.CONFIRM_PASSWORD_INPUT)
        field.clear()
        wait_random()
        slow_typing(field, password)
        wait_random()

    def click_register(self):
        wait_random()
        self.driver.find_element(*self.REGISTER_BUTTON).click()
        wait_random()

    def click_back_to_login(self):
        self.driver.find_element(*self.BACK_TO_LOGIN_BUTTON).click()

    def open_agreement_link(self):
        self.driver.find_element(*self.AGREEMENT_LINK).click()

    def open_help(self):
        self.driver.find_element(*self.HELP_LINK).click()

    def get_error_messages(self):
        elements = self.driver.find_elements(*self.ERROR_MESSAGES)
        return [e.text for e in elements if e.text.strip()]
