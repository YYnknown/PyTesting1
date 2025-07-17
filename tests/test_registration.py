import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.registration_page import RegistrationPage


def test_registration_invalid_email(driver):
    page = RegistrationPage(driver)
    page.open()

    page.enter_first_name("Умар")
    page.enter_last_name("Алиев")
    page.select_region_by_index(1)
    page.enter_email("неправильный_емейл")
    page.enter_password("Test1234")
    page.enter_confirm_password("Test1234")
    page.click_register()

    time.sleep(2)
    errors = page.get_error_messages()
    assert any("email" in e.lower() or "адрес" in e.lower() for e in errors)


def test_registration_passwords_do_not_match(driver):
    page = RegistrationPage(driver)
    page.open()

    page.enter_first_name("Умар")
    page.enter_last_name("Алиев")
    page.select_region_by_index(1)
    page.enter_email("aliyevumar@gmail.com")
    page.enter_password("Test1234")
    page.enter_confirm_password("Wrong123")
    page.click_register()

    time.sleep(2)
    errors = page.get_error_messages()
    assert any("не совпадают" in e.lower() or "парол" in e.lower() for e in errors)


def test_registration_with_weak_password(driver):
    page = RegistrationPage(driver)
    page.open()

    page.enter_first_name("Умар")
    page.enter_last_name("Алиев")
    page.select_region_by_index(1)
    page.enter_email("weakpass@gmail.com")
    page.enter_password("123")
    page.enter_confirm_password("123")
    page.click_register()

    errors = page.get_error_messages()
    assert any("слабый" in e.lower() or "недостаточно" in e.lower() or "парол" in e.lower() for e in errors)


def test_successful_registration(driver):
    page = RegistrationPage(driver)
    page.open()

    email = "lakox35234@hosintoy.com" #ЗДЕСЬ НАДО БУДЕТ ВВЕСТИ НОВУЮ ПОЧТУ
    password = "vXWpQHWT_f+4h35"

    print(f"\n Регистрируем нового пользователя: {email}")

    page.enter_first_name("Умар")
    page.enter_last_name("Алиев")
    page.select_region_by_index(1)
    page.enter_email(email)
    page.enter_password(password)
    page.enter_confirm_password(password)
    page.click_register()

    try:
        WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.ID, "rt-code-input"))
        )
        print("Введите код подтверждения вручную...")
        time.sleep(100)
    except:
        print("Поле для кода не появилось — возможно, подтверждение не требуется.")

    WebDriverWait(driver, 10).until(
        EC.url_contains("b2c.passport.rt.ru")
    )
    assert "b2c.passport.rt.ru" in driver.current_url.lower()

    driver.quit()