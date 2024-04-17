from locators.cart_locators import CartLocators
from locators.catalog_locators import CatalogLocators
from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from src.urls import Urls


class TestShoppingCart:
    url = Urls()
    cart_locators = CartLocators()
    catalog_locators = CatalogLocators()

    def test_add_to_cart_backpack_from_catalog(self, driver):
        page = CartPage(driver, self.url.base_url)
        page.open()
        page.login()
        page.add_to_cart_backpack()
        page.open_cart()
        item = page.title_of_backpack()
        assert item.is_displayed()
