import allure
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

from locators.cart_locators import CartLocators
from locators.login_locators import LoginLocators
from locators.main_locators import MainLocators
from src.user_data import UserData


class BasePage:
    timeout = 10
    login_locators = LoginLocators()
    main_locators = MainLocators()
    user = UserData()
    cart_locators = CartLocators()

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    @allure.step('login')
    def login(self):
        with allure.step('Entering username'):
            self.element_is_visible(self.login_locators.USERNAME_FIELD).send_keys(self.user.USERNAME)
        with allure.step('Entering password'):
            self.element_is_visible(self.login_locators.PASSWORD_FIELD).send_keys(self.user.PASSWORD)
        with allure.step('Clicking login button'):
            self.element_is_clickable(self.login_locators.LOGIN_BUTTON).click()

    @allure.step('open browser')
    def open(self):
        self.driver.get(self.url)


    @allure.step('get text')
    def get_text(self, locator):
        return self.element_is_visible(locator).text

    def click(self, locator):
        return self.element_is_clickable(locator).click()

    def is_displayed(self, locator):
        return self.element_is_visible(locator).is_displayed()

    def length(self, locator):
        return len(self.elements_are_visible(locator))

    def element_is_clickable(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def element_is_visible(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def open_cart(self):
        return self.element_is_clickable(self.main_locators.SHOPPING_CART).click()

    def select_by_value(self, locator, value):
        sorting = Select(self.element_is_visible(locator))
        sorting.select_by_value(value)

    def element_is_not_present(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))




