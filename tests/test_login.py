import time
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_invalid_login_and_password(driver):
    """TC-AUTH-002: Вход с невалидным логином и паролем"""
    email = "fakeuser@example.com"
    password = "wrongpass"

    login = LoginPage(driver)
    login.open()
    login.switch_to_email_tab()
    login.login(email, password)

    error = login.get_login_error_message()
    assert error is not None
    assert "неверный" in error.lower()

    time.sleep(3)

def test_valid_login_invalid_password(driver):
    """TC-AUTH-003: Вход с валидным логином и невалидным паролем"""
    email = "lakox35234@hosintoy.com"
    password = "wrongpassword"

    login = LoginPage(driver)
    login.open()
    login.switch_to_email_tab()
    login.login(email, password)

    error = login.get_login_error_message()
    assert error is not None
    assert "неверный" in error.lower()

    time.sleep(3)

def test_empty_fields(driver):
    """TC-AUTH-004: Вход с пустыми полями"""
    login = LoginPage(driver)
    login.open()
    login.switch_to_email_tab()
    login.login("", "")

    error = login.get_username_required_error()
    assert error is not None
    assert "указанный при регистрации" in error.lower() or "введите" in error.lower()

    time.sleep(3)

def test_valid_login(driver):
    """TC-AUTH-001: Успешный вход с валидными данными"""
    email = "lakox35234@hosintoy.com"  #ЗДЕСЬ НАДО БУДЕТ ВВЕСТИ НОВУЮ ПОЧТУ
    password = "vXWpQHWT_f+4h35"

    login = LoginPage(driver)
    login.open()
    login.switch_to_email_tab()
    login.login(email, password)

    WebDriverWait(driver, 10).until(
        EC.url_contains("b2c.passport.rt.ru")
    )
    assert "b2c.passport.rt.ru" in driver.current_url

    time.sleep(3)
    driver.quit()
