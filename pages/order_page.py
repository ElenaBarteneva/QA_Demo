from locators.cart_locators import CartLocators
from locators.catalog_locators import CatalogLocators
from locators.main_locators import MainLocators
from locators.order_locators import OrderLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    catalog_locators = CatalogLocators()
    main_locators = MainLocators()
    cart_locators = CartLocators()
    order_locators = OrderLocators()

    def order_with_valid_credentials(self, lst_data):
        self.add_to_cart_and_checkout()
        self.fill_the_field(lst_data[0], lst_data[1], lst_data[2])
        self.click(self.order_locators.FINISH_BTN)
        return self.get_text(self.order_locators.SUCCESSFULL_ORDER)

    def order_with_wrong_credentials(self, lst_data):
        self.add_to_cart_and_checkout()
        self.fill_the_field(lst_data[0], lst_data[1], lst_data[2])

        return self.get_text(self.order_locators.ERROR_MESSAGE)

    def add_to_cart_and_checkout(self):
        self.element_is_clickable(self.catalog_locators.ADD_TO_CART_BACKPACK).click()
        self.element_is_clickable(self.main_locators.SHOPPING_CART).click()
        self.element_is_clickable(self.cart_locators.CHECKOUT_BTN).click()

    def fill_the_field(self, first_name, last_name, postal_code):
        self.element_is_visible(self.order_locators.FIRST_NAME_FIELD).send_keys(first_name)
        self.element_is_visible(self.order_locators.LAST_NAME_FIELD).send_keys(last_name)
        self.element_is_visible(self.order_locators.ZIP_CODE).send_keys(postal_code)
        self.element_is_clickable(self.order_locators.CONTINUE_BTN).click()



