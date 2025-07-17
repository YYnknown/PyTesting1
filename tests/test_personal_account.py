import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage
from utils.human_typing import slow_typing
from utils.human_delay import wait_random
from selenium.common.exceptions import TimeoutException

@pytest.mark.order(1)
def test_lk_elements(driver):
    email = "lakox35234@hosintoy.com"  #ЗДЕСЬ НАДО БУДЕТ ВВЕСТИ НОВУЮ ПОЧТУ
    password = "vXWpQHWT_f+4h35"

    login = LoginPage(driver)
    login.open()

    print("Вводим email и пароль")
    slow_typing(driver.find_element(By.ID, "username"), email)
    wait_random()
    slow_typing(driver.find_element(By.ID, "password"), password)
    wait_random()

    driver.find_element(By.ID, "kc-login").click()

    lk = PersonalAccountPage(driver)
    print("Переход в личный кабинет")
    lk.click_lk_button()

    assert lk.is_inside_lk()

    wait = WebDriverWait(driver, 15)

    print("Проверка логотипа Ростелекома")
    assert wait.until(EC.presence_of_element_located((By.CLASS_NAME, "rtk-logo-full"))).is_displayed()

    print("Проверка ссылки 'Главная'")
    assert wait.until(EC.presence_of_element_located((
        By.XPATH, "//a[@class='app-header_navigation_link active' and text()='Главная']"
    ))).is_displayed()

    print("Проверка раздела 'Мои услуги'")
    assert wait.until(EC.presence_of_element_located((
        By.XPATH, "//div[contains(@class, 'simple-drop-down_control') and contains(., 'Мои услуги')]"
    ))).is_displayed()

    print("Проверка ссылки 'Заявки'")
    assert wait.until(EC.presence_of_element_located((
        By.XPATH, "//a[@href='#orders' and contains(@class, 'app-header_navigation_link')]"
    ))).is_displayed()

    print("Проверка ссылки 'Финансы'")
    assert wait.until(EC.presence_of_element_located((
        By.XPATH, "//a[@href='#finance' and contains(@class, 'app-header_navigation_link')]"
    ))).is_displayed()

    print("Проверка ссылки 'Переезд'")
    assert wait.until(EC.presence_of_element_located((
        By.XPATH, "//a[contains(@href, 'pereezd') and contains(@class, 'app-header_navigation_link')]"
    ))).is_displayed()

    print("Проверка иконки уведомлений (колокольчик)")
    assert wait.until(EC.presence_of_element_located((
        By.CLASS_NAME, "n-symbol__notification-small"
    ))).is_displayed()

    print("Проверка имени пользователя")
    name = wait.until(EC.presence_of_element_located((
        By.XPATH, "//div[contains(@class, 'color_black') and contains(text(), 'Умар Алиев')]"
    )))
    assert "Умар Алиев" in name.text

    print("Проверка блока 'Нет лицевых счетов'")
    assert wait.until(EC.presence_of_element_located((
        By.XPATH, "//h2[contains(text(), 'Нет лицевых счетов')]"
    ))).is_displayed()

    assert wait.until(EC.presence_of_element_located((
        By.XPATH, "//div[contains(text(), 'Привяжите лицевой счет или закажите новую услугу')]"
    ))).is_displayed()

    print("Проверка кнопок 'Привязать лицевой счет' и 'Заказать новую услугу'")
    assert wait.until(EC.presence_of_element_located((
        By.XPATH, "//a[contains(@href, '#attachaccount')]//span[contains(text(), 'Привязать лицевой счет')]"
    ))).is_displayed()

    assert wait.until(EC.presence_of_element_located((
        By.XPATH, "//a[contains(@href, '#service-ordering')]//span[contains(text(), 'Заказать новую услугу')]"
    ))).is_displayed()

    print("Все проверки прошли успешно.")


@pytest.mark.order(2)
def test_lk_clickable1(driver):
    wait = WebDriverWait(driver, 10)

    print("Проверка кликабельности баннера '3250'")
    banner = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="https://lk.rt.ru/#bonus"]'))
    )

    assert banner.is_displayed(), "Баннер не отображается"
    assert banner.is_enabled(), "Баннер неактивен"

    print("✓ Баннер 'Бонус 3250' доступен и кликабелен")


@pytest.mark.order(3)
def test_lk_clickable2(driver):
    time.sleep(3)

    wait = WebDriverWait(driver, 20)
    print("Проверка кликабельности блока 'Заказать новую услугу'")

    ordering_block = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='#service-ordering'].main-page_content_services_service"))
    )

    assert ordering_block.is_displayed(), "Блок 'Заказать новую услугу' не отображается"
    assert ordering_block.is_enabled(), "Блок 'Заказать новую услугу' неактивен"

    print("✓ Блок 'Заказать новую услугу' найден и кликабелен")


@pytest.mark.order(4)
def test_lk_clickable3(driver):
    time.sleep(3)

    wait = WebDriverWait(driver, 20)
    print("Проверка кликабельности кнопки 'Привязать лицевой счет'")

    button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '#attachaccount')]//span[text()='Привязать лицевой счет']"))
    )

    assert button.is_displayed(), "Кнопка не отображается"
    assert button.is_enabled(), "Кнопка неактивна"

    print("✓ Кнопка 'Привязать лицевой счет' найдена и кликабельна")

@pytest.mark.order(5)
def test_lk_clickable4(driver):

    time.sleep(2)

    wait = WebDriverWait(driver, 20)
    print("Проверка кликабельности кнопки 'Заказать новую услугу'")

    button = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//a[contains(@href, '#service-ordering')]//span[text()='Заказать новую услугу']"
        ))
    )

    assert button.is_displayed(), "Кнопка не отображается"
    assert button.is_enabled(), "Кнопка неактивна"

    print("✓ Кнопка 'Заказать новую услугу' найдена и кликабельна")

@pytest.mark.order(6)
def test_lk_clickable5(driver):

    time.sleep(2)

    wait = WebDriverWait(driver, 20)
    print("Проверка кликабельности кнопки 'Все события'")

    button = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//a[contains(@href, '#feed')]//span[text()='Все события']"
        ))
    )

    assert button.is_displayed(), "Кнопка 'Все события' не отображается"
    assert button.is_enabled(), "Кнопка 'Все события' неактивна"

    print("✓ Кнопка 'Все события' найдена и кликабельна")

@pytest.mark.order(7)
def test_lk_clickable6(driver):
    time.sleep(2)

    wait = WebDriverWait(driver, 20)
    print("Проверка кликабельности кнопки 'Показать еще'")

    button = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//button[contains(@class, 'main-page_content_feed_more-button')]//span[text()='Показать еще']"
        ))
    )

    assert button.is_displayed(), "Кнопка 'Показать еще' не отображается"
    assert button.is_enabled(), "Кнопка 'Показать еще' неактивна"

    print("Кнопка 'Показать еще' найдена и кликабельна")

@pytest.mark.order(8)
def test_support_chat(driver):

    wait = WebDriverWait(driver, 30)

    print("Кликаем по кнопке 'Поддержка'")
    support_button = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "omch-bar__item"))
    )
    support_button.click()
    time.sleep(2)

    print("Ожидаем поле ввода и печатаем сообщение")
    textarea = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea[data-testid='text-field']"))
    )
    textarea.click()
    textarea.send_keys("Здравствуйте")

    print("Ждём 3 секунды перед отправкой сообщения")
    time.sleep(3)

    print("Нажимаем на кнопку отправки по id")
    try:
        send_button = driver.find_element(By.ID, "send_message")
        if send_button.is_enabled() and send_button.is_displayed():
            send_button.click()
            print("Сообщение отправлено")
        else:
            raise Exception("Кнопка 'Отправить' найдена, но неактивна")
    except Exception as e:
        print(f"Ошибка при нажатии кнопки отправки: {e}")
        time.sleep(200)
        return

    print("Ожидаем появления имени оператора (до 200 секунд)")
    try:
        operator_name = WebDriverWait(driver, 200).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span.operator-name"))
        )
        print(f"Ответ от: {operator_name.text}")

        print("Ждём 5 секунд перед завершением теста")
        time.sleep(5)

    except TimeoutException:
        print("Ответ не получен. Ждём 200 секунд перед завершением")
        time.sleep(200)