import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture(autouse=True)
def reset_browser(driver, request):
    # Пропустить первый тест (например, test_successful_registration), если он первый в списке
    if request.node.name != "test_successful_registration":
        driver.refresh()
