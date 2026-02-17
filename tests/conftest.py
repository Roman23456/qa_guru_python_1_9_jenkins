import pytest
from allure_commons._allure import attach
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# @pytest.fixture(scope="function")
# def setup_browser():
#     options = Options()
#     # options.add_argument("--headless")
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")
#
#     # Для локального запуска:
#     driver = webdriver.Chrome(options=options)


@pytest.fixture(scope='function')
def setup_browser():
    options = Options()

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    #driver = webdriver.Chrome(options=options)

    yield driver

    attach.add_html(driver)
    attach.add_screenshot(driver)
    attach.add_logs(driver)