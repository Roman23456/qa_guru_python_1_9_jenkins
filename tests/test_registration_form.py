import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.registration_page import RegistrationPage


@allure.title("Successful fill form")
def test_successful(setup_browser):
    registration_page = RegistrationPage(setup_browser)


    with allure.step("Open registration form"):
        registration_page.open()
        registration_page.fill_number('1234356')
        registration_page.fill_text('wwwww')
        registration_page.fill_password('1234gj')
        registration_page.fill_date('10.08.1994')
        registration_page.click_display_inputs()