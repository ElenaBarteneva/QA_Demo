from locators.cart_locators import CartLocators
from locators.catalog_locators import CatalogLocators
from pages.base_page import BasePage


class CartPage(BasePage):
    cart_locators = CartLocators()
    catalog_locators = CatalogLocators()

    def add_to_cart_backpack(self):
        return self.element_is_clickable(self.catalog_locators.ADD_TO_CART_BACKPACK).click()

    def list_of_items(self):
        return list(self.elements_are_visible(self.cart_locators.ITEMS_LIST))

    def title_of_backpack(self):
        return self.element_is_clickable(self.catalog_locators.ITEM_NAME)