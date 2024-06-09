import random

import pytest

from functions import sort_list
from pages.main_page import MainPage
from src.main_data import MainData
from src.urls import Urls


class TestMainPage:
    url = Urls()
    main_data = MainData()

    def test_logout(self, driver):
        page = MainPage(driver, self.url.base_url)
        page.open()
        page.login()
        page.logout()
        assert driver.current_url == self.url.base_url and page.check_login_form_is_displayed() is True, \
            'Login form is not displayed'

    @pytest.mark.parametrize('value', main_data.sorting_prices)
    def test_sorting_prices(self, driver, value):
        page = MainPage(driver, self.url.base_url)
        page.open()
        page.login()
        lst = page.filter_price(value[0])
        assert lst == sort_list(lst, '$', value[1]), value[2]

    def test_item_to_cart(self, driver):
        page = MainPage(driver, self.url.base_url)
        page.open()
        page.login()
        cart_index = page.add_to_cart().text
        assert cart_index == '1', 'product amount in cart is not =1'

    def test_remove_item_from_cart(self, driver):
        page = MainPage(driver, self.url.base_url)
        page.open()
        page.login()
        page.add_to_cart()
        page.remove_from_cart()
        value = page.check_elem_is_not_present()
        assert value is True, 'The element is present in DOM'

    @pytest.mark.parametrize("value", [random.choice([1, 2, 3, 4, 5, 6])])
    def test(self, driver, value):
        page = MainPage(driver, self.url.base_url)
        page.open()
        page.login()
        page.check_card(value)