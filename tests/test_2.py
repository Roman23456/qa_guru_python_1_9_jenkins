import allure
from pages.citylink_page import CitiLinkPage


@allure.title("Форма регистрации")
def test_successful(setup_browser):
    actionlink_page = CitiLinkPage(setup_browser)

    with allure.step("Открываем страницу"):
        actionlink_page.open()

    with allure.step('Клик на кнопку войти'):
        actionlink_page.click_login()

    with allure.step('Ввод номера телефона'):
        actionlink_page.fill_number('79897678548')