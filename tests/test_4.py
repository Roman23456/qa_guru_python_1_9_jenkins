import allure
from pages.citylink_page import CitiLinkPage


@allure.title("Фильтрация")
def test_successful(setup_browser):
    actionlink_page = CitiLinkPage(setup_browser)

    with allure.step("Открываем сайт"):
        actionlink_page.open()

    with allure.step('Просмотр фильтров'):
        actionlink_page.go_to_stores_section()