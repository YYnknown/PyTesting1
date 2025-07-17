# PyTesting1

Автоматизированные UI-тесты для сайта Ростелеком, реализованные с использованием `Selenium` и `pytest`.

---

## Установка зависимостей

Для корректной работы проекта необходимо установить следующие библиотеки:


```
selenium==4.16.0
pytest==8.1.1
webdriver-manager==4.0.2
pytest-order==1.3.0
```

## Команды для выполнения тестов

```
pytest tests/test_registration.py
pytest tests/test_login.py::test_valid_login
pytest tests/test_login.py::test_invalid_login_and_password
pytest tests/test_login.py::test_valid_login_invalid_password
pytest tests/test_login.py::test_empty_fields
pytest tests/test_personal_account.py -s
```

## Список тест-кейсов

Список тест-кейсов доступен по ссылке 

```
[Google Docs — Тест-кейсы](https://docs.google.com/spreadsheets/d/1gT26dILuOISx339RxpNSAEwHrfA7b_QKlpOJBozDexc/edit?usp=sharing)
```