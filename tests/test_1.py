import allure
from pages.citylink_page import CitiLinkPage


@allure.title("Открытие страницы")
def test_successful(setup_browser):
    actionlink_page = CitiLinkPage(setup_browser)

    with allure.step("Открываем страницу"):
        actionlink_page.open()


