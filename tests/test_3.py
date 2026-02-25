
import allure
from pages.citylink_page import CitiLinkPage


@allure.title("Поиск по инпуту")
def test_successful(setup_browser):
    actionlink_page = CitiLinkPage(setup_browser)

    with allure.step("Открываем сайт"):
        actionlink_page.open()

    with allure.step('Поиск техники'):
        actionlink_page.search_input('Ноутбуки')
