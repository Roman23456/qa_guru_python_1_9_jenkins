
import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CitiLinkPage:
    URL = 'https://www.citilink.ru/'
    number = '79778847690'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=30)

    @allure.step('Open url')
    def open(self):
        self.driver.get(self.URL)

    @allure.step('Click login button')
    def click_login(self):
        element = WebDriverWait(self.driver, timeout=30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-meta-name="UserButtonContainer"]'))
        )
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Ввод номера телефона')
    def fill_number(self, number):  # С параметром
        element = WebDriverWait(self.driver, timeout=30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="phone"]'))
        )
        element.clear()
        element.send_keys(number)

        button = WebDriverWait(self.driver, timeout=30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]'))
        )
        # Скроллим к элементу
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        self.driver.execute_script("arguments[0].click();", button)

    @allure.step('Поиск в инпуте')
    def search_input(self, name):
        element = WebDriverWait(self.driver, timeout=30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="text"]'))
        )
        element.click()

        element = WebDriverWait(self.driver, timeout=30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="text"]'))
        )
        element.send_keys(name)
        element.send_keys(Keys.ENTER)

    @allure.step('Перейти в раздел Магазины')
    def go_to_stores_section(self):
        element = WebDriverWait(self.driver, timeout=30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/about/stores/"]'))
        )
        element.click()

        # Проверка по заголовку h1 или h4
        page_loaded = WebDriverWait(self.driver, timeout=30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'h1, h4, [class*="Heading"]'))
        )
        assert "Адреса магазинов" in page_loaded.text or "5POST" in page_loaded.text, \
            f"Страница магазинов не загрузилась. Текст: {page_loaded.text}"

    @allure.step('Перейти в раздел каталог')
    def go_to_catalog(self):
        element = WebDriverWait(self.driver, timeout=30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/catalog/"]'))
        )
        element.click()

        element = WebDriverWait(self.driver, timeout=30).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[contains(text(), "Электроинструменты")]'))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

        # Проверка что страница Электроинструменты загрузилась
        page_loaded = WebDriverWait(self.driver, timeout=30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'h1, [class*="Heading"]'))
        )
        assert "Электроинструменты" in page_loaded.text, \
            f"Страница Электроинструменты не загрузилась. Текст: {page_loaded.text}"

