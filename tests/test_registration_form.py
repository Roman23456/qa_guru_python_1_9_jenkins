import allure

from pages.registration_page import RegistrationPage


def test_registration_form(setup_browser):
    registration_page = RegistrationPage(setup_browser)

    with allure.step('Fill form'):
        registration_page.open()
        registration_page.fill_number('1234356')
        registration_page.fill_text('wwwww')
        registration_page.fill_password('1234qj')
        registration_page.fill_date('10.08.1994')
        registration_page.click_display_inputs()


