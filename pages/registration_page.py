import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class RegistrationPage:
    URL = "https://practice.expandtesting.com/inputs"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Open url")
    def open(self):
        self.driver.get(self.URL)

    @allure.step('number')
    def fill_number(self, number):
        element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID, "input-number"))
        )
        element.clear()
        element.send_keys(number)

    @allure.step('Text')
    def fill_text(self,text):
        element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID, "input-text"))
        )
        element.clear()
        element.send_keys(text)

    @allure.step('Password')
    def fill_password(self, password):
        element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID, "input-password"))
        )
        element.clear()
        element.send_keys(password)

    @allure.step('date')
    def fill_date(self, date):
        element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID, "input-date"))
        )
        element.clear()
        element.send_keys(date)

    @allure.step("Click Display Inputs button")
    def click_display_inputs(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btn-display-inputs"))
        )
        element.click()

