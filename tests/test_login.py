from locators.login_locators import LoginLocators
from locators.main_locators import MainLocators
from pages.login_page import LoginPage
from src.urls import Urls


class TestLogin:
    url = Urls()
    main_locators = MainLocators()
    login_locators = LoginLocators()

    def test_login_title_isdisplayed(self, driver):
        page = LoginPage(driver, self.url.base_url)
        page.open()
        page.login()
        actual_text = page.get_text(self.main_locators.TITLE)
        expected_text = 'Products'
        assert actual_text == expected_text, \
            f'Unexpected text Actual text: {actual_text}, expected text: {expected_text}'

    def test_login_product_cards(self, driver):
        page = LoginPage(driver, self.url.base_url)
        page.open()
        page.login()
        expected_len = 6
        cards = page.length(self.main_locators.PRODUCTS)
        assert cards == expected_len, \
            f'Unexpected length, expected len: {expected_len}, actual len: {cards}'

    def test_login_logout_isdiplayed(self, driver):
        page = LoginPage(driver, self.url.base_url)
        page.open()
        page.login()
        page.click(self.main_locators.BURGER_MENU)
        assert page.is_displayed(self.main_locators.LOGOUT), 'Logout button is nt displayed'

    def test_login_redirect(self, driver):
        page = LoginPage(driver, self.url.base_url)
        page.open()
        page.login()
        assert driver.current_url == 'https://www.saucedemo.com/inventory.html', 'url не соответствует ожидаемому'

    def test_login_wrong_credentials(self, driver):
        page = LoginPage(driver, self.url.base_url)
        page.open()
        page.login_with_wrong_credentials()
        expected_error_text = 'Epic sadface: Username and password do not match any user in this service'
        actual_error_text = page.get_text(self.login_locators.ERROR_LOGIN)
        assert expected_error_text == actual_error_text, \
            f'Unexpected text of error, expected text: {expected_error_text}, actual text: {actual_error_text}'
