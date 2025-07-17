from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.human_delay import wait_random
import requests


class PersonalAccountPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.LK_BUTTON = (By.ID, "lk-btn")

    def click_lk_button(self):
        self.wait.until(EC.element_to_be_clickable(self.LK_BUTTON))
        wait_random()
        self.driver.find_element(*self.LK_BUTTON).click()

    def is_inside_lk(self):
        self.wait.until(lambda d: "lk.rt.ru" in d.current_url)
        return "lk.rt.ru" in self.driver.current_url
