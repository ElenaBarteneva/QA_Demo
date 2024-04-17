from locators.catalog_locators import CatalogLocators
from locators.login_locators import LoginLocators
from locators.main_locators import MainLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    main_locators = MainLocators()
    login_locators = LoginLocators()
    catalog_locators = CatalogLocators()

    def logout(self):
        self.click(self.main_locators.BURGER_MENU)
        self.click(self.main_locators.LOGOUT)

    def check_login_form_is_displayed(self):
        return self.is_displayed(self.login_locators.LOGIN_FORM)

    def select(self, value):
        locator = self.main_locators.SORTING
        self.select_by_value(locator=locator, value=value)

    def get_price(self):
        lst = self.elements_are_visible(self.main_locators.PRODUCT_PRICES)
        lst_price = [i.text for i in lst]
        return lst_price

    def filter_price(self, value):
        self.select(value)
        return self.get_price()

    def add_to_cart(self):
        self.click(self.catalog_locators.ADD_TO_CART_BACKPACK)
        return self.element_is_visible(self.main_locators.SHOPPING_CART)

    def remove_from_cart(self):
        self.click(self.catalog_locators.REMOVE_FROM_CART)

    def check_elem_is_not_present(self):
        return self.element_is_not_present(self.main_locators.COUNT_ITEMS)




