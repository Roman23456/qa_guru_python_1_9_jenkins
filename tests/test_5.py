
import allure
from pages.citylink_page import CitiLinkPage


@allure.title("Просмотр каталога товаров")
def test_successful(setup_browser):
    actionlink_page = CitiLinkPage(setup_browser)

    with allure.step("Открываем сайт"):
        actionlink_page.open()

    with allure.step('Открываем магазины'):
        actionlink_page.go_to_catalog()