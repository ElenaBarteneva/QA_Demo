from locators.login_locators import LoginLocators
from pages.base_page import BasePage
from src.user_data import UserData


class LoginPage(BasePage):
    locators = LoginLocators()
    user = UserData()

    def login_with_wrong_credentials(self):
        self.element_is_visible(self.locators.USERNAME_FIELD).send_keys(self.user.INVALID_USERNAME)
        self.element_is_visible(self.locators.PASSWORD_FIELD).send_keys(self.user.INVALID_PASSWORD)
        self.element_is_clickable(self.locators.LOGIN_BUTTON).click()

